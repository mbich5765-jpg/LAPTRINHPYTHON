import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def bai_1_bang_cuu_chuong(a, b):
    start = min(a, b)
    end = max(a, b)
    for i in range(start, end + 1):
        print(f"Bảng cửu chương {i}:")
        for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")

def bai_2_kiem_tra_nguyen_to(n):
    if is_prime(n):
        print(f"{n} là số nguyên tố.")
    else:
        print(f"{n} không phải là số nguyên tố.")

def bai_3_liet_ke_nguyen_to(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(str(i))
    if primes:
        print(f"Các số nguyên tố nhỏ hơn {n} là: {', '.join(primes)}")
    else:
        print(f"Không có số nguyên tố nào nhỏ hơn {n}.")

def bai_4_dem_nguyen_to(n):
    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += 1
    print(f"Số lượng các số nguyên tố nhỏ hơn {n} là: {count}")

def bai_5_uoc_so_nguyen_to(n):
    prime_divisors = []
    for i in range(1, n + 1):
        if n % i == 0 and is_prime(i):
            prime_divisors.append(str(i))
    if prime_divisors:
        print(f"Các số vừa là ước số của {n}, vừa là số nguyên tố: {', '.join(prime_divisors)}")
    else:
        print(f"Không có ước số nào của {n} là số nguyên tố.")

def main():
    chuoi_nhap = input("Nhập a, b: ")
    a, b = map(int, chuoi_nhap.split(','))
    bai_1_bang_cuu_chuong(a, b)
    
    n2 = int(input("Nhập n bài 2: "))
    bai_2_kiem_tra_nguyen_to(n2)
    
    n3 = int(input("Nhập n bài 3: "))
    bai_3_liet_ke_nguyen_to(n3)
    
    n4 = int(input("Nhập n bài 4: "))
    bai_4_dem_nguyen_to(n4)
    
    n5 = int(input("Nhập n bài 5: "))
    bai_5_uoc_so_nguyen_to(n5)

if __name__ == "__main__":
    main()