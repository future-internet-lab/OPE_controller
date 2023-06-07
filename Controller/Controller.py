import socket
import yaml
import time
import random
import os
from _thread import *
from SenderHelper import *
from Connection import Connect
from Processor import Processor

with open("config.yml", "r") as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        exit()

PID = os.getpid()
print(PID)

host = config['controller']['address']['host']
port = config['controller']['address']['port']
num_client = config['client']['num']

def StartController(session_id):
    # Init
    SendToAll(proc.Clients, b'\x00', b'\x00', session_id, b'\x00', b'')


if __name__ == "__main__":
    proc = Processor(PID, num_client)
    ServerSideSocket = socket.socket() # create socket
    ThreadCount = 0                    # thread count
    try:
        ServerSideSocket.bind((host, port)) # connect
    except socket.error as e:
        print(str(e))
        exit()
    print('Socket is listening..')
    ServerSideSocket.listen(num_client)

    session_id = random.randint(0,255).to_bytes(2, 'big')

    while True:
        client, address = ServerSideSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(Connect, (client, proc ))
        proc.Clients.append(client)
        ThreadCount += 1
        if ThreadCount >= num_client:
            time.sleep(0.5)
            # Start the controller
            StartController(session_id)

    ServerSideSocket.close()