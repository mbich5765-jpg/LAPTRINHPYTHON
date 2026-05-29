def kiem_tra_nguyen_to(n):
    # Trả về True nếu là số nguyên tố, ngược lại là False
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def dem_nguyen_to_nho_hon(n):
    # Đếm số lượng số nguyên tố < n
    count = 0
    for i in range(2, n):
        if kiem_tra_nguyen_to(i):
            count += 1
    return count

def uoc_so_nguyen_to(n):
    # Tìm các ước số của n đồng thời là số nguyên tố
    uoc_nt = []
    for i in range(2, n + 1):
        if n % i == 0 and kiem_tra_nguyen_to(i):
            uoc_nt.append(i)
    return uoc_nt

if __name__ == "__main__":
    # Yêu cầu 1: Kiểm tra số nguyên tố
    n1 = int(input("Nhập số nguyên dương n (để kiểm tra): "))
    if kiem_tra_nguyen_to(n1):
        print(f"{n1} là số nguyên tố.")
    else:
        print(f"{n1} không phải là số nguyên tố.")

    # Yêu cầu 2: Đếm số nguyên tố < n
    n2 = int(input("\nNhập số nguyên dương n (để đếm): "))
    print(f"Số lượng các số nguyên tố nhỏ hơn {n2} là: {dem_nguyen_to_nho_hon(n2)}")

    # Yêu cầu 3: Liệt kê ước là số nguyên tố
    n3 = int(input("\nNhập số nguyên dương n (để tìm ước nguyên tố): "))
    ket_qua = uoc_so_nguyen_to(n3)
    
    # Dùng join để in mảng ra chuỗi 
    chuoi_ket_qua = ", ".join(map(str, ket_qua))
    print(f"Các số vừa là ước số của {n3}, vừa là số nguyên tố: {chuoi_ket_qua}")