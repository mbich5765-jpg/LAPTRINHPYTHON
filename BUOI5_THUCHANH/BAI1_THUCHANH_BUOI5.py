import math

# Hàm dùng chung để kiểm tra số nguyên tố
def is_prime(num):
    if num < 2:
        return False
    # Lặp đến căn bậc 2 (sqrt) để tối ưu tốc độ
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def bai_1_bang_cuu_chuong(a, b):
    # Dùng min, max phòng hờ người dùng nhập số lớn trước
    start = min(a, b)
    end = max(a, b)
    for i in range(start, end + 1):
        print(f"\n--- Bảng cửu chương {i} ---")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")

def bai_2_kiem_tra_nguyen_to(n):
    if is_prime(n):
        print(f"=> {n} là số nguyên tố.")
    else:
        print(f"=> {n} không phải là số nguyên tố.")

def bai_3_liet_ke_nguyen_to(n):
    mang_nt = [] # Mảng lưu kết quả
    for i in range(2, n):
        if is_prime(i):
            mang_nt.append(str(i)) # Ép kiểu chuỗi để lát dùng hàm join
            
    if len(mang_nt) > 0:
        print(f"=> Các số nguyên tố nhỏ hơn {n}: {', '.join(mang_nt)}")
    else:
        print(f"=> Không có số nguyên tố nào nhỏ hơn {n}.")

def bai_4_dem_nguyen_to(n):
    dem = 0 
    for i in range(2, n):
        if is_prime(i):
            dem += 1
    print(f"=> Có tổng cộng {dem} số nguyên tố nhỏ hơn {n}")

def bai_5_uoc_so_nguyen_to(n):
    mang_uoc = []
    # Kiểm tra chia hết (dư 0) VÀ là số nguyên tố
    for i in range(1, n + 1):
        if n % i == 0 and is_prime(i):
            mang_uoc.append(str(i))
            
    if len(mang_uoc) > 0:
        print(f"=> Ước số vừa là số nguyên tố của {n}: {', '.join(mang_uoc)}")
    else:
        print(f"=> Không có ước số nguyên tố nào.")

def main():
    # split(',') để cắt chuỗi tại dấu phẩy
    chuoi_nhap = input("Nhập 2 số a, b (cách nhau dấu phẩy): ")
    a, b = map(int, chuoi_nhap.split(','))
    bai_1_bang_cuu_chuong(a, b)
    
    print("-" * 30)
    n2 = int(input("Bài 2 - Nhập n: "))
    bai_2_kiem_tra_nguyen_to(n2)
    
    print("-" * 30)
    n3 = int(input("Bài 3 - Nhập n: "))
    bai_3_liet_ke_nguyen_to(n3)
    
    print("-" * 30)
    n4 = int(input("Bài 4 - Nhập n: "))
    bai_4_dem_nguyen_to(n4)
    
    print("-" * 30)
    n5 = int(input("Bài 5 - Nhập n: "))
    bai_5_uoc_so_nguyen_to(n5)

if __name__ == "__main__":
    main()