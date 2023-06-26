import socket
from Processor import Processor


def Connect(connection: socket.socket, proc: Processor):
    """
    Hàm xử lý logic luồng bản tin nhận
    :param connection: socket với client
    :param proc: Module Processor
    """
    connection.send(str.encode('Server is working'))
    while True:
        data = connection.recv(65536)
        if not data:
            break
        print(data)  # test
        if len(data) >= 8:
            options = data[5]
            if options & 0b10000000:
                if options & 0b01000000:  # Đọc bit error
                    print("error!")
                elif options & 0b00100000:  # Đọc bit warning
                    print("warning!")
                else:
                    # ok, it's good. Logic here
                    if data[0] == 0:
                        print('Server receive data[0]= ', data[0])
                        proc.ProcessInit(data) #send 2
                    if data[0] == 1:
                        print('Server receive data[0]= ', data[0])
                        proc.ProcessRunService(data) # send 5
                    if data[0] == 2:
                        print('Server receive data[0]= ', data[0])
                        proc.ProcessSendingCode(data)  #send 1
                    if data[0] == 3:
                        proc.ProcessRequestLOG(data)
                        print('Request file from Client . . .')
                    if data[0] == 4:
                        print('Server receive data[0]= ', data[0])
                        proc.ProcessKillService(data)
                    if data[0] == 5:
                        print('Server receive data[0]= ', data[0])
                        proc.ProcessTerminate(data) # stop

    connection.close()
