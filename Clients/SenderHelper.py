

def DDCPformat(ContentType: bytes, \
                Version: bytes, \
                SessionID: bytes, \
                ClientID: bytes, \
                Options: bytes, \
                Payload: bytes):
    return ContentType + Version + SessionID + ClientID.to_bytes(1, 'big') + Options + len(Payload).to_bytes(2, 'big') + Payload