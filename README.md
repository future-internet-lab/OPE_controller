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
