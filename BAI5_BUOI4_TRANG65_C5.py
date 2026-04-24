def Fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return Fibonacci(n - 1) + Fibonacci(n - 2)

n = int(input("Nhập số nguyên dương n: "))
print(f"Số hạng thứ {n} của chuỗi Fibonacci là: {Fibonacci(n)}")