
# print('Helloworld')

# for i in range(5):
#     print(i)

# # while True:
# #     for i in range(5):
# #         print(i)

import os

# Nhập tên thư mục mới từ người dùng
folder_name = "Log_folder"

# Tạo thư mục mới
os.mkdir(folder_name)
print(f"Đã tạo thư mục '{folder_name}'")

# Tạo đường dẫn cho file txt
file_path = os.path.join(folder_name, "new_file.txt")

# Mở file txt và ghi nội dung vào
with open(file_path, "w") as file:
    file.write("Đây là nội dung của log file txt mới")

print(f"Đã tạo file '{file_path}'")