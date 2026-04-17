n = int(input("Nhập số nguyên dương n: "))
tong = 0
tich = 1

while n > 0:
    digit = n % 10
    tong += digit
    tich *= digit
    n //= 10

print(f"tổng={tong}, tích={tich}")