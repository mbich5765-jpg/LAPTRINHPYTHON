def doi_tien(x):
    menh_gia = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    tong_so_to = 0

    print(f"So tien {x} duoc doi thanh:")
    
    for tien in menh_gia:
        so_to = x // tien
        print(f"Loai {tien} gom {so_to} to")
        
        tong_so_to += so_to
        
        x = x % tien

    print(f"TỔNG CỘNG CÓ {tong_so_to} TỜ")

so_tien_nhap_vao = int(input("Mời bạn nhập số tiền X cần đổi: "))

doi_tien(so_tien_nhap_vao)