import math

# Dùng hàm abs() tính trị tuyệt đối
bai_1 = lambda n: abs(n)

bai_2 = lambda n: n + 15

bai_3 = lambda x, y: x * y

# Chia lấy dư (%) bằng 0
bai_4 = lambda n: n % 13 == 0 or n % 19 == 0

# Diện tích = Pi * r^2
bai_5 = lambda r: math.pi * (r ** 2)

# Chu vi = (dài + rộng) * 2
bai_6 = lambda d, r: 2 * (d + r)

# Căn bậc 2 bình phương lên bằng chính nó
bai_7 = lambda n: n >= 0 and math.isqrt(n)**2 == n

# Dùng hàm all() kiểm tra không chia hết cho số nào
bai_8 = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))

# Do dùng lambda nên phải lồng if...else liên tiếp trên 1 dòng
bai_9 = lambda a, b, c: (
    "Không phải tam giác" if a + b <= c or a + c <= b or b + c <= a else
    "Tam giác đều" if a == b == c else
    "Tam giác vuông cân" if (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2) and (a == b or a == c or b == c) else
    "Tam giác vuông" if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 else
    "Tam giác cân" if a == b or a == c or b == c else
    "Tam giác thường"
)

def main():
    n1 = int(input("Bài 1 - Nhập n: "))
    print(f"=> Trị tuyệt đối: {bai_1(n1)}\n")
    
    n2 = int(input("Bài 2 - Nhập n: "))
    print(f"=> Kết quả n + 15: {bai_2(n2)}\n")
    
    chuoi_3 = input("Bài 3 - Nhập x, y (cách nhau dấu phẩy): ")
    x3, y3 = map(int, chuoi_3.split(','))
    print(f"=> Tích 2 số: {bai_3(x3, y3)}\n")
    
    n4 = int(input("Bài 4 - Nhập n: "))
    print(f"=> Là bội của 13 hoặc 19: {bai_4(n4)}\n")
    
    r5 = float(input("Bài 5 - Nhập bán kính r: "))
    print(f"=> Diện tích hình tròn: {bai_5(r5)}\n")
    
    chuoi_6 = input("Bài 6 - Nhập chiều dài, rộng (cách nhau dấu phẩy): ")
    d6, r6 = map(float, chuoi_6.split(','))
    print(f"=> Chu vi hình chữ nhật: {bai_6(d6, r6)}\n")
    
    n7 = int(input("Bài 7 - Nhập n: "))
    print(f"=> Là số chính phương: {bai_7(n7)}\n")
    
    n8 = int(input("Bài 8 - Nhập n: "))
    print(f"=> Là số nguyên tố: {bai_8(n8)}\n")
    
    chuoi_9 = input("Bài 9 - Nhập 3 cạnh a, b, c (cách nhau dấu phẩy): ")
    a9, b9, c9 = map(int, chuoi_9.split(','))
    print(f"=> Phân loại: {bai_9(a9, b9, c9)}\n")

if __name__ == "__main__":
    main()