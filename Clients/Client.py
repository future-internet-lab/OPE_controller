import socket
import yaml
from _thread import *

with open("config.yml", "r") as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        exit()

host = config['controller']['address']['host']
port = config['controller']['address']['port']

client_id = None
session_id = None

if __name__ == "__main__":
    Client = socket.socket()
    print('Waiting for connection response')
    try:
        Client.connect((host, port))
    except socket.error as e:
        print(str(e))
        exit()

    data = Client.recv(1024)
    Client.send(b'Hello')
    while True:
        data = Client.recv(65536)
        print(data)
        if (len(data) >= 8):
            options = data[5]
            if not (options & 0b10000000):
                if options & 0b01000000:
                    print("error!")
                elif options & 0b00100000:
                    print("warning!")
                else:
                    # ok, it's good. Xử lý logic gói request
                    if data[0] == 0:    # Initiation
                        client_id = data[4]
                        session_id = data[2:4]
                        Client.send(b'\x00\x00'+session_id+client_id.to_bytes(1,'big')+b'\x80\x00\x00')
                    if data[0] == 1:    # Run service
                        # TODO: next flow
                        print('None')
                    if data[0] == 2:    # Send code
                        # TODO: next flow
                        print('None')