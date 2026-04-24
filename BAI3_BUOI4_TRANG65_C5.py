def TinhLuyThua(a, b):
    if b == 0:
        return 1
    return a * TinhLuyThua(a, b - 1)

a = int(input("Nhập số nguyên dương a (cơ số): "))
b = int(input("Nhập số nguyên dương b (số mũ): "))
print(f"Kết quả {a}^{b} là: {TinhLuyThua(a, b)}")