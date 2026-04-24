from math import sqrt

cau_a = lambda n: n if n >= 0 else -n

cau_b = lambda n: n + 15

cau_c = lambda x, y: x * y

cau_d = lambda n: "Là bội số" if (n % 13 == 0 or n % 19 == 0) else "Không là bội số"

cau_e = lambda r: 3.14159 * r * r

cau_f = lambda d, r: (d + r) * 2

cau_g = lambda n: "Là số chính phương" if n > 0 and int(sqrt(n))**2 == n else "Không là số chính phương"

def LaSNT(x):
    if x <= 1:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

cau_h = lambda n: "Là số nguyên tố" if LaSNT(n) == True else "Không là số nguyên tố"

def KiemTraTamGiac(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Tam giác đều"
        elif a == b or b == c or a == c:
            if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
                return "Tam giác vuông cân"
            return "Tam giác cân"
        elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
            return "Tam giác vuông"
        else:
            return "Tam giác thường"
    else:
        return "Không phải 3 cạnh hợp lệ của tam giác"

cau_i = lambda a, b, c: KiemTraTamGiac(a, b, c)


print("Kết quả câu a (Trị tuyệt đối của -10):", cau_a(-10))
print("Kết quả câu b (n + 15 với n=5):", cau_b(5))
print("Kết quả câu c (Tích 4 và 5):", cau_c(4, 5))
print("Kết quả câu d (Kiểm tra số 38):", cau_d(38))
print("Kết quả câu e (Diện tích tròn r=3):", cau_e(3))
print("Kết quả câu f (Chu vi HCN d=4, r=2):", cau_f(4, 2))
print("Kết quả câu g (Kiểm tra số 16):", cau_g(16))
print("Kết quả câu h (Kiểm tra số 7):", cau_h(7))
print("Kết quả câu i (Kiểm tra 3 cạnh 3, 4, 5):", cau_i(3, 4, 5))