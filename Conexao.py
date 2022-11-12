ServerIP = input("Server IP: ")

# var para coletar porta aberta no servidor
PORT = int(input("Port: "))

# inicia o client socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    # var que recebe o nome escolhido pelo usuário
    username = input('Enter a username: ')

    # inicia a conexão com o servidor 
    client.connect((ServerIP,PORT))

    # se a conexão der certo printa que a conexão deu certo, IP e porta da conexão
    print(f'Connected Successfully to {ServerIP}:{PORT}')
except:

    # se a conexão falhar entra num loop dizendo que teve erro na conexão
    print(f'ERROR: Please review your input: {ServerIP}:{PORT}')

# função para receber a mensagem
def receiveMessage():
    while True:
        try:
            # var que recebe a mensagem vinda do servidor decodificada
            message = client.recv(2048).decode('ascii')

            # envia o nome do usuário para servidor
            if message=='getUser':
                client.send(username.encode('ascii'))
            
            elif message=='Name already exists on the server':
                thread1.daemon = True
                thread2.daemon = True
                sys.exit()
            # 
            elif message[:2] == "ID" or message[:4] == "NOME" or message[:9] == "SOBRENOME" or message[:7] == "APELIDO" or message[:5] == "EMAIL" or message[:3] == "CPF":
                print(message, end=" || ")
            else:
                print(message, end="\n")
        except:
            print('ERROR: Check your connection or server might be offline')

def sendMessage():
    while True:
        client.send(input().encode('ascii'))

thread1 = threading.Thread(target=receiveMessage,args=()) 
