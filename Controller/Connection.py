import socket
from Processor import Processor

def Connect(connection: socket.socket, proc: Processor):
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
                    if data[0] == 5:
                        proc.ProcessTerminate(data)
        
    connection.close()