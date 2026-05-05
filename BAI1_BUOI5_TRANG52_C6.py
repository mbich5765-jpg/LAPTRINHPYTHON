import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    L = []
    while True:
        try:
            so = int(input("Nhập một số nguyên: "))
            L.append(so) 
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ!")
            continue
            
        tiep_tuc = input("Bạn có muốn nhập nữa không? (Yes/No hoặc Y/N): ").strip().upper()
        if tiep_tuc == 'N' or tiep_tuc == 'NO':
            break

    if not L:
        print("Danh sách rỗng!")
        return

    print(f"\nDanh sách bạn vừa nhập: {L}")

    # a) In ra các số nguyên tố có trong list
    so_nguyen_to = list(filter(lambda x: is_prime(x), L))
    print(f"a) Các số nguyên tố có trong list là: {so_nguyen_to}")

    # b) Tính trung bình cộng các số âm, trung bình các số dương
    so_am = [x for x in L if x < 0]
    so_duong = [x for x in L if x > 0]
    
    if len(so_am) > 0:
        print(f"b) Trung bình cộng các số âm: {sum(so_am) / len(so_am)}")
    else:
        print("b) Không có số âm nào trong danh sách để tính trung bình.")

    if len(so_duong) > 0:
        print(f"   Trung bình cộng các số dương: {sum(so_duong) / len(so_duong)}")
    else:
        print("   Không có số dương nào trong danh sách để tính trung bình.")
  
    # c) Số lớn nhất, số nhỏ nhất
    print(f"c) Số lớn nhất trong list: {max(L)}")
    print(f"   Số nhỏ nhất trong list: {min(L)}")

    # d) Cho biết các số trong list có được sắp xếp tăng dần hay chưa?
    L_sorted = L.copy()
    L_sorted.sort()

    if L == L_sorted:
        print("d) Các số trong list ĐÃ được sắp xếp tăng dần.")
    else:
        print("d) Các số trong list CHƯA được sắp xếp tăng dần.")

if __name__ == "__main__":
    main()