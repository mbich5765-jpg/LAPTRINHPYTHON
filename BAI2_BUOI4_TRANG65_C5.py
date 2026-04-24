def GiaiThua(n):
    if n == 1:
        return 1
    return GiaiThua(n - 1) * n

n = int(input("Nhập số nguyên dương n: "))
print(f"Giai thừa của {n} (tức là {n}!) là: {GiaiThua(n)}")