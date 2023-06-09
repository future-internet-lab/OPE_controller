def DDCPformat(ContentType: bytes,
               Version: bytes,
               SessionID: bytes,
               ClientID: int,
               Options: bytes,
               Payload: bytes):
    """
    Hàm hỗ trợ chuyển sang dạng DDCP
    :param ContentType: Loại hành động thực hiện trong giao thức
    :param Version: Phiên bản của protocol
    :param SessionID: ID của phiên kết nối
    :param ClientID: ID của kết nối với client
    :param Options: Các trường bit option hỗ trợ cho protocol
    :param Payload: Nội dung đi kèm protocol
    :return:
    """
    return ContentType + Version + SessionID + ClientID.to_bytes(1, 'big') + Options + len(Payload).to_bytes(2, 'big') + Payload
