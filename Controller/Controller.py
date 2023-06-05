import socket
import yaml
import time
import random
from _thread import *
from SenderHelper import *
from Processor import Processor

with open("config.yml", "r") as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        exit()

host = config['controller']['address']['host']
port = config['controller']['address']['port']
num_client = config['client']['num']

proc = Processor(num_client)

def Connect(connection):
    global proc
    connection.send(str.encode('Server is working'))
    while True:
        data = connection.recv(65536)
        if not data:
            break
        print(data)     # test
        if (len(data) >= 8):
            options = data[5]
            if options & 0b10000000:
                if options & 0b01000000:    # Đọc bit error
                    print("error!")
                elif options & 0b00100000:  # Đọc bit warning
                    print("warning!")
                else:
                    # ok, it's good. Logic here
                    if data[0] == 0:
                        proc.ProcessInit(data)
                    if data[0] == 2:
                        proc.ProcessSendingCode(data)
        
    connection.close()

def StartController(session_id):
    # Init
    SendToAll(proc.Clients, b'\x00', b'\x00', session_id, b'\x00', b'')


if __name__ == "__main__":
    ServerSideSocket = socket.socket()

    ThreadCount = 0
    try:
        ServerSideSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
        exit()
    print('Socket is listening..')
    ServerSideSocket.listen(num_client)

    session_id = random.randint(0,255).to_bytes(2, 'big')

    while True:
        client, address = ServerSideSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(Connect, (client, ))
        proc.Clients.append(client)
        ThreadCount += 1
        if ThreadCount >= num_client:
            time.sleep(0.5)
            # Start the controller
            StartController(session_id)

    ServerSideSocket.close()