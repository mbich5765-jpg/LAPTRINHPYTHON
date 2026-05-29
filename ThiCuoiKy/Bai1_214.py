# Nhập dữ liệu đầu vào
chieu_dai = float(input("Nhập chiều dài đáy hình khối chữ nhật (cm):>? "))
chieu_rong = float(input("Nhập chiều rộng đáy hình khối chữ nhật (cm):>? "))
chieu_cao = float(input("Nhập chiều cao hình khối chữ nhật (cm):>? "))
so_le = int(input("Số lượng số lẻ cần hiển thị:>? "))

# Xử lý tính toán
dien_tich_day = chieu_dai * chieu_rong
the_tich = dien_tich_day * chieu_cao

# Xuất kết quả
# Sử dụng định dạng :.{so_le}f để làm tròn động theo số lượng số lẻ đã nhập
# Sử dụng mã Unicode \u00b2 và \u00b3 cho ký tự số mũ
print(f"Diện tích đáy hình chữ nhật = {dien_tich_day:.{so_le}f} cm\u00b2")
print(f"Thể tích hình khối= {the_tich:.{so_le}f} cm\u00b3")