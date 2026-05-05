from collections import Counter

def main():
    
    S1 = input("Nhập chuỗi S1: ")
    S2 = input("Nhập chuỗi S2: ")
    # a) In ra những ký tự xuất hiện trong cả 2 chuỗi
    c1 = Counter(S1)
    c2 = Counter(S2)
    
    ky_tu_chung = c1 & c2
    
    danh_sach_chung = list(ky_tu_chung.keys())
    print(f"\na) Các ký tự xuất hiện trong cả 2 chuỗi là: {danh_sach_chung}")

    dict1 = dict.fromkeys(S1)
    dict2 = dict.fromkeys(S2)

    s1_not_s2 = [char for char in dict1 if char not in dict2]
    
    s2_not_s1 = [char for char in dict2 if char not in dict1]

    # b) Đếm xem có bao nhiêu ký tự có trong S1 nhưng không có trong S2
    tong_so_luong = len(s1_not_s2) + len(s2_not_s1)
    print(f"\nb) Tổng số lượng ký tự có trong chuỗi này nhưng không có trong chuỗi kia là: {tong_so_luong}")

    # c) In ra những ký tự có trong S1 nhưng không có trong S2 
    print("\nc) Chi tiết các ký tự khác biệt:")
    print(f"   - Có trong S1 nhưng không có trong S2: {s1_not_s2}")
    print(f"   - Có trong S2 nhưng không có trong S1: {s2_not_s1}")

if __name__ == "__main__":
    main()