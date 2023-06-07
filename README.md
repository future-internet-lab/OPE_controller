# OPE_controller

Khối điều khiển **Optimization Parallelism Efficiency Controller** với giao thức **Distributed DNN Controller Protocol**

![image](https://github.com/future-internet-lab/OPE_controller/assets/95759699/bdde271b-2951-4f29-845b-0279f8b2350d)

## Cấu hình

Trong file `yml` trên mỗi loại thiết bị:

- `controller`: Cấu hình cho controller. Gồm địa chỉ IP và port (mặc định 823)
- `client`: Số lượng thiết bị client được điều khiển

## Chạy chương trình

Controller:
```
cd Controller/
python3 Controller.py
```

Các Clients:
```
cd Clients/
python3 Client.py
```

# Distributed DNN Controller Protocol

DDCP record format:

![image](https://github.com/future-internet-lab/OPE_controller/assets/95759699/41827ef9-7687-41e9-acfb-49d314c551b3)

Các trường trong DDCP:

- **Content type**: Loại hành động thực hiện trong giao thức
- **Version**: Phiên bản của protocol
- **Session ID**: ID của phiên kết nối
- **End-to-end ID**: ID của thiết bị liên kết với controller
- **Options**: Các trường bit option hỗ trợ cho protocol
- **Length**: Chiều dài byte của payload bản tin
- **Payload**: Nội dung đi kèm protocol trong một số content type cụ thể

## Content type:

| Byte | Tên | Mục đích | Payload | Payload ACK |
|---|---|---|---|---|
| 0x00 | Initiation | Khởi tạo controller với các clients | None \| Cấu hình | None \| Cấu hình |
| 0x01 | Run service | Chạy chương trình Torch Disitrbuted | Lệnh thực hiện | None \| Chi tiết lỗi |
| 0x02 | Send code | Gửi code Torch Distributed (mạng DNN đã phân tán) | Code Torch Distributed | None |
| 0x03 | Request logging data | Yêu cầu kết quả time, memory từ client | None | Logging data |
| 0x04 | Kill service | Dừng process Torch Distributed | None | None |
| 0x05 | Terminate | Dừng tất cả | None | None |
| 0x06 | Request parameters | Yêu cầu các parameters | None | Các parameters |
| ... | ... | (Phát triển trong tương lai) |  |  |

## Options:

| Bit | Tên | Mục đích gắn (1) |
|---|---|---|
| 0 | Ack | Khi gói tin là ACK |
| 1 | Error | Khi có lỗi từ phía gửi |
| 2 | Warning | Khi có cảnh báo từ phía gửi |
| ... | ... | (Phát triển trong tương lai) |