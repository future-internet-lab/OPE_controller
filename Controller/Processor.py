from SenderHelper import *
import os
import time

Duration_time = 30

class Processor:
    def __init__(self, pid: int, num_client: int):
        self.pid = pid
        self.count = 0
        self.num_client = num_client
        self.Clients = []

        self._check = [False] * num_client

    def IsContinue(self) -> bool:
        for i in self._check:
            if not i:
                return False
        return True

    def ResetCheck(self):
        for _ in self._check:
            _ = False

    # def sendFile(self):
    # for

    def ProcessInit(self, mess: bytes):
        """
        Xử lý khi nhận gói tin Initiation ACK
        :param mess: Gói tin nhận được
        :return: None
        """
        userId = mess[4]
        try:
            self._check[userId] = True
        except:
            print("Error while reading message")
            return
        if self.IsContinue():
            # gui file wo day
            with open("code_generator/Helloworld.py", "r") as f:
                payload = f.read().encode("utf-8")
            # Send Code (2) with payload
            print(payload)
            SendToAll(self.Clients, b'\x02', b'\x00', mess[2:4], b'\x00', payload)
            self.ResetCheck()

    def ProcessRunService(self, mess:bytes):
        userId = mess[4]
        try:
            self._check[userId] = True
        except:
            print("Error while reading message")
        if self.IsContinue():
            print('Client is running code ...')
            time.sleep(Duration_time)
            SendToAll(self.Clients, b'\x03', b'\x00', mess[2:4], b'\x00', b'')

    def ProcessSendingCode(self, mess: bytes):
        """
        Xử lý khi nhận gói tin Send Code ACK
        :param mess: Gói tin nhận được
        :return: None
        """
        userId = mess[4]
        try:
            self._check[userId] = True
        except:
            print("Error while reading message")
            return
        if self.IsContinue():
            # TODO: thành luồng chạy code, đang để Terminate (5)
            print(mess)
            SendToAll(self.Clients, b'\x01', b'\x00', mess[2:4], b'\x00', b'')
            self.ResetCheck()

    def ProcessRequestLOG(self, mess:bytes):
        userId = mess[4]
        try:
            self._check[userId] = True
        except:
            print("Error while reading message")
            return
        if self.IsContinue():
            # TODO: thành luồng chạy code, đang để Terminate (5)
            print('Client receive mess[0]= ', mess[0])
            payload_len = int(mess[6]) * 256 + int(mess[7])
            payload = mess[8:(8 + payload_len)]
            f = open("log_receiver/log1.txt", "w")
            f.write(payload.decode("utf-8"))
            f.close()
            SendToAll(self.Clients, b'\x04', b'\x00', mess[2:4], b'\x00', b'')

    def ProcessKillService(self, mess:bytes):
        print("Kill all service . . .")
        SendToAll(self.Clients, b'\x05', b'\x00', mess[2:4], b'\x00', b'')

    def ProcessTerminate(self, mess: bytes):
        """
         Xử lý khi nhận gói tin Terminate ACK
        :param mess: Gói tin nhận được
        :return: None
        """
        # Tạm thời dừng flow
        userId = mess[4]
        try:
            self._check[userId] = True
        except:
            print("Error while reading message")
            return
        if self.IsContinue():
            print("Stop controller")
            os.system("sudo kill " + str(self.pid))
