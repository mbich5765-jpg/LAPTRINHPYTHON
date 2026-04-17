
# BÀI TẬP 5.3 trang (40)
chieu_dai = float(input(" nhập chiều dài đáy hình chữ nhật (cm) :>? "))
chieu_rong = float(input(" Nhập chiều rộng đáy hình c2hữ nhật (cm) :>?"))
chieu_cao = float(input (" Nhập chiều cao hình khối chữ nhật (cm) :>?"))
so_le = int(input("Số lượng số lẻ cần hiển thị:>? "))
dien_tich_day = chieu_dai * chieu_rong
the_tich = dien_tich_day * chieu_cao 


print("Diện tích đáy hình chữ nhật = {0:.{1}f}cm\u00b2".format(dien_tich_day, so_le)) # này là công  thức có sẵn trong file trang (35) 
print("Thể tích hình khối= {0:.{1}f}cm\u00b3".format(the_tich, so_le))# này là công  thức có sẵn trong file trang (35) 


