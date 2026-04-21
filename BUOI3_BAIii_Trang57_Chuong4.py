from datetime import datetime


ngay1_str = input("Nhập ngày thứ nhất (định dạng ngày/tháng/năm, vd 18/09/2019): ")
ngay2_str = input("Nhập ngày thứ hai (định dạng ngày/tháng/năm, vd 20/09/2019): ")

ngay1 = datetime.strptime(ngay1_str, "%d/%m/%Y")
ngay2 = datetime.strptime(ngay2_str, "%d/%m/%Y")


khoang_cach = abs(ngay2 - ngay1)

print(f"Số ngày cách nhau giữa 2 ngày là: {khoang_cach.days} ngày")