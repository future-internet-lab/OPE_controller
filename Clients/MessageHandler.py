import socket
import os
from SenderHelper import *


class MessageHandler:
    def __init__(self, client: socket.socket, pid: int):
        self.client = client
        self.client_id = None
        self.session_id = None
        self.pid = pid

    def process(self, mess: bytes):
        """
        Xử lý bản tin nhận được phía client
        :param mess: Bản tin nhận được
        """
        if len(mess) >= 8:
            options = mess[5]
            if not (options & 0b10000000):
                if options & 0b01000000:
                    print("error!")
                elif options & 0b00100000:
                    print("warning!")
                else:
                    # ok, it's good. Xử lý logic gói request
                    if mess[0] == 0:  # Initiation
                        self.client_id = mess[4]
                        self.session_id = mess[2:4]
                        self.client.send(DDCPformat(b'\x00', b'\x00', self.session_id, self.client_id, b'\x80', b''))
                    if mess[0] == 1:  # Run service
                        # TODO: next flow
                        print('None')
                    if mess[0] == 2:  # Send code
                        # TODO: Nhận code ở đây
                        payload_len = int(mess[6]) * 256 + int(mess[7])
                        payload = mess[8:(8 + payload_len)]
                        f = open("code_receiver/receive1.py", "w")
                        f.write(payload.decode("utf-8"))
                        f.close()
                        self.client.send(DDCPformat(b'\x02', b'\x00', self.session_id, self.client_id, b'\x80', b''))
                    if mess[0] == 5:  # Terminate
                        # TODO: Nhận code ở đây
                        self.client.send(DDCPformat(b'\x05', b'\x00', self.session_id, self.client_id, b'\x80', b''))
                        os.system("sudo kill " + str(self.pid))
