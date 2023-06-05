# OPE_controller

Khối điều khiển **Optimization Parallelism Efficiency Controller** với giao thức **Distributed DNN Controller Protocol**

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