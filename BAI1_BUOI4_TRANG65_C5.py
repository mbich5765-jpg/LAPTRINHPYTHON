def TongChuSo(n):
    n = abs(n)
    if n == 0:
        return 0
    return (n % 10) + TongChuSo(n // 10)

n = int(input("Nhập số nguyên n: "))
print(f"Tổng các chữ số của {n} là: {TongChuSo(n)}")