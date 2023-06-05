

def DDCPformat(ContentType, Version, SessionID, ClientID, Options, Payload):
    return ContentType + Version + SessionID + ClientID.to_bytes(1, 'big') + Options + len(Payload).to_bytes(2, 'big') + Payload