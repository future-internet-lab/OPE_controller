

def SendToAll(Clients: list,
              ContentType: bytes,
              Version: bytes,
              SessionID: bytes,
              Options: bytes,
              Payload: bytes) -> None:
    """
    Gửi toàn bộ dữ liệu cho các clients
    :param Clients: List các socket client để gửi tới
    :param ContentType: Loại hành động thực hiện trong giao thức
    :param Version: Phiên bản của protocol
    :param SessionID: ID của phiên kết nối
    :param Options: Các trường bit option hỗ trợ cho protocol
    :param Payload: Nội dung đi kèm protocol
    """
    for id, c in enumerate(Clients):
        c.send(ContentType + Version + SessionID + id.to_bytes(1, 'big') + Options + len(Payload).to_bytes(2,'big') + Payload)