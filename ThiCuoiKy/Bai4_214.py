# Khai báo các hàm ẩn danh (lambda) trả về boolean
is_square = lambda x: int(x**0.5)**2 == x
is_perfect = lambda x: x > 1 and sum(i for i in range(1, (x // 2) + 1) if x % i == 0) == x

# 1. In các số chính phương
print("Các số chính phương từ 1 đến 10000:")
for i in range(1, 10001):
    if is_square(i):
        print(i, end=" ")

print("\n\n" + "-"*50 + "\n")

# 2. In các số hoàn thiện
print("Các số hoàn thiện từ 1 đến 10000:")
for i in range(1, 10001):
    if is_perfect(i):
        print(i, end=" ")