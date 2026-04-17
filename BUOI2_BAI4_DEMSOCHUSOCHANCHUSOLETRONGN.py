n = int(input("Nhập số nguyên dương n: "))
so_chan = 0
so_le = 0

while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        so_chan += 1
    else:
        so_le += 1
    n //= 10

print("Số lượng số chẵn:", so_chan)
print("Số lượng số lẻ:", so_le)