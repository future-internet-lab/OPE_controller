from SenderHelper import *

class Processor:
    def __init__(self, num_client):
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

    """
    Xử lý khi nhận gói tin Initiation ACK
    """
    def ProcessInit(self, mess):
        userId = mess[4]
        self._check[userId] = True
        if self.IsContinue():
            # Send Code (2), chưa có payload
            SendToAll(self.Clients, b'\x02', b'\x00', mess[2:4], b'\x00', b'')
            self.ResetCheck()

    """
    Xử lý khi nhận gói tin Send Code ACK
    """
    def ProcessSendingCode(self, mess):
        return None


