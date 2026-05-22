import math

is_friendly = lambda n: math.gcd(n, int(str(n)[::-1])) == 1

is_perfect_square = lambda n: math.isqrt(n)**2 == n

is_repdigit_v1 = lambda n: n > 0 and all(d == str(n)[0] for d in str(n))

is_repdigit_v2 = lambda n: n > 0 and not any(d != str(n)[0] for d in str(n))

is_perfect = lambda n: n > 1 and sum(i for i in range(1, n // 2 + 1) if n % i == 0) == n

is_abundant = lambda n: n > 0 and sum(i for i in range(1, n // 2 + 1) if n % i == 0) > n

is_increasing = lambda n: all(int(str(n)[i]) <= int(str(n)[i+1]) for i in range(len(str(n))-1))

is_armstrong = lambda n: sum(int(d)**len(str(n)) for d in str(n)) == n

is_prime_c1 = lambda n: n > 1 and sum(1 for i in range(1, n + 1) if n % i == 0) == 2

is_prime_c2 = lambda n: n > 1 and sum(i for i in range(1, n + 1) if n % i == 0) == n + 1

is_prime_c3 = lambda n: False if n <= 1 else not any(n % i == 0 for i in range(2, math.isqrt(n) + 1))

def F(k):
    if k <= 1:
        return False
    return len(list(filter(lambda i: k % i == 0, range(2, math.isqrt(k) + 1)))) == 0

is_palindrome = lambda n: str(n) == str(n)[::-1]

is_prime_palindrome = lambda n: n > 1 and str(n) == str(n)[::-1] and not any(n % i == 0 for i in range(2, math.isqrt(n) + 1))

is_locphat_c1 = lambda n: all(d in '68' for d in str(n))

is_locphat_c2 = lambda n: str(n).count('6') + str(n).count('8') == len(str(n))

is_locphat_palindrome = lambda n: all(d in '68' for d in str(n)) and str(n) == str(n)[::-1]

if __name__ == "__main__":
    while True:
        print("\n--- CHỌN CHẾ ĐỘ ---")
        print("1. Kiểm tra các điều kiện của một số")
        print("2. In các số thoả mãn trong một khoảng tự chọn")
        print("0. Thoát")
        
        choice = input("Nhập lựa chọn của bạn: ")
        
        if choice == '0':
            break
            
        elif choice == '1':
            try:
                n = int(input("\nNhập một số nguyên dương để kiểm tra: "))
                print(f"a) Số thân thiện: {is_friendly(n)}")
                print(f"b) Số chính phương: {is_perfect_square(n)}")
                print(f"c) Số đồng nhất: {is_repdigit_v1(n)}")
                print(f"d) Số hoàn thiện: {is_perfect(n)}")
                print(f"e) Số phong phú: {is_abundant(n)}")
                print(f"f) Số tăng dần: {is_increasing(n)}")
                print(f"g) Số Armstrong: {is_armstrong(n)}")
                print(f"h) Số nguyên tố: {is_prime_c3(n)}")
                print(f"i) Số Palindrome: {is_palindrome(n)}")
                print(f"j) Số nguyên tố Palindrome: {is_prime_palindrome(n)}")
                print(f"k) Số lộc phát: {is_locphat_c1(n)}")
                print(f"l) Số lộc phát Palindrome: {is_locphat_palindrome(n)}")
            except ValueError:
                print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")
                
        elif choice == '2':
            try:
                start = int(input("\nNhập giá trị bắt đầu: "))
                end = int(input("Nhập giá trị kết thúc: "))
                
                print(f"\nCác số lộc phát palindrome từ {start} đến {end} là:")
                for i in range(start, end + 1):
                    if is_locphat_palindrome(i):
                        print(i, end=" ")
                print()
            except ValueError:
                print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")