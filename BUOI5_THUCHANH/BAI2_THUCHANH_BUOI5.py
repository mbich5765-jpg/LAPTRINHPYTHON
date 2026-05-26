import math

bai_1 = lambda n: abs(n)

bai_2 = lambda n: n + 15

bai_3 = lambda x, y: x * y

bai_4 = lambda n: n % 13 == 0 or n % 19 == 0

bai_5 = lambda r: math.pi * (r ** 2)

bai_6 = lambda d, r: 2 * (d + r)

bai_7 = lambda n: n >= 0 and math.isqrt(n)**2 == n

bai_8 = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))

bai_9 = lambda a, b, c: (
    "Không phải tam giác" if a + b <= c or a + c <= b or b + c <= a else
    "Tam giác đều" if a == b == c else
    "Tam giác vuông cân" if (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2) and (a == b or a == c or b == c) else
    "Tam giác vuông" if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2 else
    "Tam giác cân" if a == b or a == c or b == c else
    "Tam giác thường"
)

def main():
    n1 = int(input("Bài 1 - Nhập số nguyên n: "))
    print(bai_1(n1))
    
    n2 = int(input("Bài 2 - Nhập số nguyên n: "))
    print(bai_2(n2))
    
    chuoi_3 = input("Bài 3 - Nhập 2 số nguyên x, y (cách nhau bởi dấu phẩy): ")
    x3, y3 = map(int, chuoi_3.split(','))
    print(bai_3(x3, y3))
    
    n4 = int(input("Bài 4 - Nhập số nguyên n: "))
    print(bai_4(n4))
    
    r5 = float(input("Bài 5 - Nhập số thực r (bán kính): "))
    print(bai_5(r5))
    
    chuoi_6 = input("Bài 6 - Nhập số thực d, r (cách nhau bởi dấu phẩy): ")
    d6, r6 = map(float, chuoi_6.split(','))
    print(bai_6(d6, r6))
    
    n7 = int(input("Bài 7 - Nhập số nguyên n: "))
    print(bai_7(n7))
    
    n8 = int(input("Bài 8 - Nhập số nguyên n: "))
    print(bai_8(n8))
    
    chuoi_9 = input("Bài 9 - Nhập 3 số nguyên a, b, c (cách nhau bởi dấu phẩy): ")
    a9, b9, c9 = map(int, chuoi_9.split(','))
    print(bai_9(a9, b9, c9))

if __name__ == "__main__":
    main()