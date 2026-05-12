def doi_tien(x):
    menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    tong_so_to = 0
    tong_so_loai = 0 

    print(f"So tien {x} duoc doi thanh:")
    
    for tien in menh_gia:
        so_to = x // tien
        
        if so_to > 0:
            print(f"Loai {tien} gom {so_to} to")
            tong_so_to += so_to
            tong_so_loai += 1 
            
        x = x % tien

    print(f"TỔNG CỘNG CÓ {tong_so_to} TỜ")
    print(f"Tong so loai = {tong_so_loai}")

print("--- CHƯƠNG TRÌNH THU NGÂN ---")
a = int(input("Nhập số tiền hàng cần phải trả (a): "))
b = int(input("Nhập số tiền khách hàng thực tế trả (b): "))

print("-" * 30) 

if a > b:
    print(f"Số tiền khách hàng còn thiếu là: {a - b}")
elif a == b:
    print("Cám ơn khách hàng. Hẹn gặp lại")
else:
    tien_thoi = b - a
    print(f"Số tiền cần thối lại cho khách là: {tien_thoi}")
    
    doi_tien(tien_thoi)
    
    input("\n(Nhấn phím Enter để hoàn tất giao dịch...)")
    print("Cám ơn khách hàng. Hẹn gặp lại")