n = int(input("Nhập số nguyên dương n: "))
tam = n
may_man = True

while tam > 0:
    digit = tam % 10
    if digit != 6 and digit != 8:
        may_man = False
        break
    tam //= 10

if may_man:
    print(f"{n} là số may mắn.")
else:
    print(f"{n} KHÔNG phải số may mắn.")