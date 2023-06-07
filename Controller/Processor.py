from SenderHelper import *
import os

class Processor:
    def __init__(self, pid, num_client):
        self.pid = pid
        self.count = 0
        self.num_client = num_client
        self.Clients = []

        self._check = [False]*num_client

    def IsContinue(self):
        for i in self._check:
            if i == False:
                return False
        return True

    def ResetCheck(self):
        for i in self._check:
            i = False

    #def sendFile(self):
        #for 

    """
    Xử lý khi nhận gói tin Initiation ACK
    """
    def ProcessInit(self, mess):
        userId = mess[4]
        try:
            self._check[userId] = True
        except:
            print("Error while reading message")
            return
        if self.IsContinue():
            # gui file wo day
            with open ("code_generator/Helloworld.py", "r") as f:
                payload = f.read().encode("utf-8")
            # Send Code (2) with payload
            print(payload)
            SendToAll(self.Clients, b'\x02', b'\x00', mess[2:4], b'\x00', payload)
            self.ResetCheck()

    """
    Xử lý khi nhận gói tin Send Code ACK
    """
    def ProcessSendingCode(self, mess):
        userId = mess[4]
        try:
            self._check[userId] = True
        except:
            print("Error while reading message")
            return
        if self.IsContinue():
            # TODO: thành luồng chạy code, đang để Terminate (5)
            SendToAll(self.Clients, b'\x05', b'\x00', mess[2:4], b'\x00', b'')
            self.ResetCheck()

    """
    Xử lý khi nhận gói tin Terminate ACK
    """
    def ProcessTerminate(self, mess):
        # Tạm thời dừng flow
        userId = mess[4]
        try:
            self._check[userId] = True
        except:
            print("Error while reading message")
            return
        if self.IsContinue():
            print("Stop controller")
            os.system("sudo kill "+str(self.pid))