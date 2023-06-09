

def SendToAll(Clients: list, \
                ContentType: bytes, \
                Version: bytes, \
                SessionID: bytes, \
                Options: bytes, \
                Payload: bytes):
    for id,c in enumerate(Clients):
        c.send(ContentType + Version + SessionID + id.to_bytes(1, 'big') + Options + len(Payload).to_bytes(2,'big') + Payload)