from ctypes.wintypes import SIZE
from importlib.metadata import metadata
import os
from pyfiglet import Figlet  
pyf = Figlet(font= 'puffy')
a = pyf.renderText('UDP Chat App with Multi-Threading')
os.system('tput setaf 3')
print(a)

import socket, cv2, pickle, struct, threading, time, pyaudio

#Socket Create 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Socket Accept
def sender():
    time.sleep(15)
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print('Host IP:',host_ip)   #Adicionar o IP
    port =      #Adicionar o caminho da porta
    socket_address = (host_ip,port)
    
    #socket Bind
    s.bind(socket_address)
    
    #socket listen
    s.listen(5)
    print('Listening at:',socket_address)
    while True:
        client_socket,addr = s.accept()
        print('Connection to:',addr)
        if client_socket:
            vid = cv2.VideoCapture(0)
            
            while (vid.isopened()):
                ret,image = vid.read()
                img_serialize = pickle.dumps(image)
                message = struct.pack('Q',len(img_serialize))+img_serialize
                client_socket.sendall(message)
                
                cv2.imshow('Video from server', image)
                key = cv2.waitkey(10)
                if key == 13:
                    client_socket.close()
                    

                #Audio 
                chunk = 1024
                FORMAT = pyaudio.paInt16            
                CHANNELS = 1
                RATE = 44100  
                
                p = pyaudio.PyAudio ()               
                
                stream = p.open(format = FORMAT,
                    channels = CHANNELS,
                    rate = RATE,
                    input = True,
                    frames_per_buffer = chunk)
    
            #Audio Socket Initialization
            audioSocket = socket.socket()
            port1 = 5000
            audioSocket.bind((<192.168.56.1>, port1))            #Adicionar o IP
            audioSocket.listen(5)
            cAudio, addr = audioSocket.accept()
            
            def recordAudio():
                time.sleep(5)
                while True:
                    data = stream.read(chunk)
                    if data:
                        cAudio.sendall(data)
                        
            def rcvAudio():
                while True:
                    audioData = audioSocket.recv(SIZE)
                    stream.write(audioData)
                    
            def connect_server():
                host_ip = '<IP>'
                port = #Adicionar porta
                s.connect((host_ip, port))
                data = b""
                metadata_size = struct.calcsize("Q")
                while True:
                    while len(data) < metadata_size:
                        packet = s.recv(4*1024)
                        if not packet: break
                        data+=packet
                    packet_msg_size = data[:metadata_size]
                    data = data[metadata_size:]
                    msg_size = struct.unpack("Q", packet_msg_size) [0]
                    
                    while len(data) < msg_size:
                        data += s.recv(4*1024)
                    frame_data = data[:msg_size]
                    data = data[msg_size:]
                    frame = pickle.loads(frame_data)
                    cv2.imshow("Receiving Video",frame)
                    key = cv2.waitkey(10)
                    if key == 13:
                        break
                    s.close()
                    
                    x1 = threading.Thread(target=sender)
                    x2 = threading.Thread(target=connect_server)
                    x3 = threading.Thread(target=recordAudio)
                    x4 = threading.Thread(target=rcvAudio)
                    
                    #start a thread
                    x1.start()
                    x2.start()
                    x3.start()
                    x4.start()


from ctypes.wintypes import SIZE
import os 
from pyfiglet import Figlet       
pyf = Figlet(font= 'puffy')
a = pyf.renderText('UDP Chat App with Multi-Threading')
os.system('tput setaf 3')
print(a)

import socket, cv2, pickle, struct, threading, time, pyaudio

#Socket Create
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def connect_server():
    time.sleep(15)
    host_ip = ''    #Adicionar o IP
    port =      #Adicionar porta
    s.connect((host_ip,port))
    data = b''
    metadata_size = struct.calcsize('Q')
    while True:
        while len(data) < metadata_size:
            packet = s.recv(4*1024)
            if not packet : break
            data+=packet
        packed_msg_size = data[:metadata_size]
        data = data[metadata_size:]
        msg_size = struct.unpack('Q',packed_msg_size) [0]
        
        while len (data) < msg_size:
            data += s.recv (4*1024)
            frame_data = data[:msg_size]
            data = data[msg_size:]
            frame = pickle.loads(frame_data)
            cv2.imshow('Receiving Video', frame)
            key = cv2.waitkey(10)
            if key == 13:
                break
            s.close()
            
        def sender ():
            host_name = socket.gethostname()
            host_ip = socket.gethostbyname(host_name)
            print('Host IP:',host_ip)
            port = 1234
            socket_address = (host_ip,port)
            #Socket Bind
            s.bind(socket_address)
            #Socket listen
            s.listem(5)
            print('Listening at:',socket_address)
            while True:
                client_socket,addr = s.accept()
                print('connected to:',addr)
                if client_socket:
                    vid = cv2.VideoCapture(1)
                    
                    while(vid.isOpened()):
                        ret,image = vid.read()
                        img_serialize = pickle.dumps(image)
                        message = struct.pack('Q',len(img_serialize))+img_serialize
                        client_socket.sendall(message)
                        
                        cv2.imshow('Video from server',image)
                        key = cv2.waitKey(10)
                        if key ==13:
                            client_socket.close()
                            
                #Audio
                chunk = 1024
                FORMAT = pyaudio.paInt16            
                CHANNELS = 1
                RATE = 44100  
                
                p = pyaudio.PyAudio()               
                
                stream = p.open(format = FORMAT,
                                channels = CHANNELS,
                                rate = RATE,
                                input = True,
                                frames_per_buffer = chunk)
                
                #Audio Socket Initialization
                audioSocket = socket.socket()
                port1 =         #Adicionar porta
                audioSocket.bind((<>, port1))            #adicionar o IP
                audioSocket.listen(5)
                cAudio, addr = audioSocket.accept()
                
                def recordAudio ():
                    time.sleep(5)
                    while True:
                        data = stream.read(chunk)
                        if data:
                            cAudio.sendall(data)
                            
                def rcvAudio ():
