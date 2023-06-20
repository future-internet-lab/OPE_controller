import yaml
from _thread import *
from MessageHandler import *

with open("config.yml", "r") as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        exit()

host = config['controller']['address']['host']
port = config['controller']['address']['port']

PID = os.getpid()
print(PID)

if __name__ == "__main__":
    Client = socket.socket()
    print('Waiting for connection response')
    try:
        Client.connect((host, port))
    except socket.error as e:
        print(str(e))
        exit()
        
    handler = MessageHandler(Client, PID)

    data = Client.recv(1024)
    Client.send(b'Client send: Hello')
    while True:
        data = Client.recv(65536)
        print(data)
        handler.process(data)
        