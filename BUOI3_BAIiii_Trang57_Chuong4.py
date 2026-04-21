from datetime import datetime


chuoi_ngay = input("Nhập chuỗi ngày (ví dụ: Sep 18 2019 2:43PM): ")

ngay_da_chuyen = datetime.strptime(chuoi_ngay, '%B %d %Y %I:%M%p')

print("Chuỗi bạn vừa nhập:", chuoi_ngay)
print("Kiểu datetime sau khi chuyển:", ngay_da_chuyen)
print("Kiểu dữ liệu:", type(ngay_da_chuyen))