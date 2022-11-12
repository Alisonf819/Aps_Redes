
from pyfiglet import Figlet, os

os.system('clear')
pyf = Figlet(font='puffy')
a = pyf.renderText('Aplicativo de bate-papo por video sem multithreading')
b = pyf.renderText('Server')
os.system('tput setaf 3')
print(a)

import socket, cv2, pickle,struct

#socket create
server_socket = socket.socket(socket.AF_INEF,socket.SOCK_STREAM)
host_name = socket.gethostname ()
host_ip = socket.gethostbyname(host_name)
print('HOST IP:192.168.56.1' ,host_ip) #Adicionar o IP
port =   #Adicionar o caminho da porta

socket_address = (host_ip,port)

#Socket Bind
server_socket.bind(socket_address)

#Socket Listen
server_socket.listen(1)
print('Listening at:',socket_address)

#Socket Accept
while True:
    client_socket,addr = server_socket.accept()
    print('Connected to:',addr)
    if client_socket:
        vid =cv2.VideoCapture(0)
        
        while(vid.isOpened()):
            ret, image = vid.read()
            img_serialize = pickle.dumps(image)
            message = struct.pack('Q',len(img_serialize))+img_serialize
            client_socket.sendall(message)
            
            cv2.imshow('Video from Server',image)
            key = cv2.waitkey(10)
            if key ==13:
                client_socket.close()
 HOST = input("Host: ")
        PORT = int(input("Port: "))

        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((HOST,PORT))
        server.listen()
        print(f'Server is Up and Listening on {HOST}:{PORT}')

        clients = []
        usernames = []

    def dadosDB(id, client):
    con = mysql.connector.connect(host='localhost', database='MYSQL_PYTHON',user='root',password='root')
    if con.is_connected():
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Tabela_Dados;")

        for (ID, NOME, SOBRENOME, APELIDO, EMAIL, CPF) in cursor:
            if str(id) == str(ID):
                getDB(f'{usernames[clients.index(client)]}: {ID}'.encode('ascii'))
                getDB(f'{usernames[clients.index(client)]}: {NOME}'.encode('ascii'))
                getDB(f'{usernames[clients.index(client)]}: {SOBRENOME}'.encode('ascii'))
                getDB(f'{usernames[clients.index(client)]}: {APELIDO}'.encode('ascii'))
                getDB(f'{usernames[clients.index(client)]}: {EMAIL}'.encode('ascii'))
                getDB(f'{usernames[clients.index(client)]}: {CPF}'.encode('ascii'))

def globalMessage(message):
    for client in clients:
        if usernames[clients.index(client)] != message[:len(usernames[clients.index(client)])].decode('ascii'):
            if message[len(usernames[clients.index(client)])+2:len(usernames[clients.index(client)])+2+2].decode('ascii') != "ID" or message[len(usernames[clients.index(client)])+2:len(usernames[clients.index(client)])+2+4].decode('ascii') != "NOME" or message[len(usernames[clients.index(client)])+2:len(usernames[clients.index(client)])+2+9].decode('ascii') != "SOBRENOME" or message[len(usernames[clients.index(client)])+2:len(usernames[clients.index(client)])+2+7].decode('ascii') != "APELIDO" or message[len(usernames[clients.index(client)])+2:len(usernames[clients.index(client)])+2+5].decode('ascii') != "EMAIL" or message[len(usernames[clients.index(client)])+2:len(usernames[clients.index(client)])+2+3].decode('ascii') != "CPF":
                client.send(message)

def getDB(message):
    for client in clients:
        if usernames[clients.index(client)] == message[:len(usernames[clients.index(client)])].decode('ascii'):
            message = message.decode('ascii')
            message = message[len(usernames[clients.index(client)])+2:].encode('ascii')
            client.send(message)

def handleMessages(client):
    while True:
        try:
            receiveMessageFromClient = client.recv(2048).decode('ascii')
            if receiveMessageFromClient[:5] == "getid":
                try:
                    dadosDB(receiveMessageFromClient[6:], client)
                except:
                    print("id não existe")
                    
            else:
                globalMessage(f'{usernames[clients.index(client)]}: {receiveMessageFromClient}'.encode('ascii'))
        except:
            clientLeaved = clients.index(client)
            client.close()
            clients.remove(clients[clientLeaved])
            clientLeavedUsername = usernames[clientLeaved]
            print(f'{clientLeavedUsername} has left the chat...')
            globalMessage(f'{clientLeavedUsername} has left us...'.encode('ascii'))
            usernames.remove(clientLeavedUsername)

def initialConnection():
    while True:
        try:
            client, address = server.accept()
            print(f"New Connetion: {str(address)}")
            clients.append(client)
            client.send('getUser'.encode('ascii'))
            username = client.recv(2048).decode('ascii')
            if not username in usernames:
                usernames.append(username)
                globalMessage(f'{username} just joined the chat!'.encode('ascii'))
                user_thread = threading.Thread(target=handleMessages,args=(client,))
                user_thread.start()
            else: 
                clients.remove(client)
                client.send('Name already exists on the server'.encode('ascii'))
        except:
            pass

initialConnection()
