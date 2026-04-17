n = int(input("Nhập số nguyên dương n: "))
lon_nhat = 0

while n > 0:
    digit = n % 10
    if digit > lon_nhat:
        lon_nhat = digit
    n //= 10

print(f"số lớn nhất={lon_nhat}")