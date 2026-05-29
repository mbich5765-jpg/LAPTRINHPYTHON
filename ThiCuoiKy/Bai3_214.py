# 1. Lambda kiểm tra số chính phương
# Điều kiện: n >= 0 và bình phương của phần nguyên căn bậc 2 bằng chính nó
kiem_tra_chinh_phuong = lambda n: n >= 0 and int(n**0.5)**2 == n

# 2. Lambda kiểm tra và phân loại tam giác
# Sử dụng if-else lồng nhau (ternary operators) để gom logic vào một hàm lambda
kiem_tra_tam_giac = lambda a, b, c: (
    "Không phải 3 cạnh hợp lệ của tam giác" if not (a + b > c and a + c > b and b + c > a) else
    "Tam giác Đều" if a == b == c else
    "Tam giác Vuông Cân" if (a == b or b == c or a == c) and (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2) else
    "Tam giác Cân" if a == b or b == c or a == c else
    "Tam giác Vuông" if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 else
    "Tam giác Thường"
)

if __name__ == "__main__":
    # Yêu cầu 1: Kiểm tra số chính phương
    print("--- KIỂM TRA SỐ CHÍNH PHƯƠNG ---")
    n = int(input("Nhập số nguyên n: "))
    if kiem_tra_chinh_phuong(n):
        print(f"-> {n} là số chính phương.")
    else:
        print(f"-> {n} không phải là số chính phương.")

    # Yêu cầu 2: Kiểm tra loại tam giác
    print("\n--- KIỂM TRA LOẠI TAM GIÁC ---")
    a = int(input("Nhập cạnh a: "))
    b = int(input("Nhập cạnh b: "))
    c = int(input("Nhập cạnh c: "))
    
    ket_qua = kiem_tra_tam_giac(a, b, c)
    print(f"-> Kết quả: {ket_qua}")