import os

file_goc = 'test.txt'
file_nen = 'test_compressed.txt' 

print("--- (1) XUẤT RA FILE MỚI GIẢM DUNG LƯỢNG (HƯỚNG 2) ---")

with open(file_goc, 'r', encoding='utf-8') as f:
    van_ban = f.read()

cac_tu = van_ban.replace('\n', ' <XUONG_DONG> ').split(' ')

tu_dien = [] 
vi_tri = []  

for tu in cac_tu:
    if tu == '': 
        continue 
        
    if tu not in tu_dien:
        tu_dien.append(tu)
        
    vi_tri.append(str(tu_dien.index(tu)))

with open(file_nen, 'w', encoding='utf-8') as f:
    f.write(",".join(tu_dien) + "\n")
    f.write(" ".join(vi_tri))

dung_luong_goc = os.path.getsize(file_goc)
dung_luong_nen = os.path.getsize(file_nen)

print(f"-> Dung lượng file gốc: {dung_luong_goc} bytes")
print(f"-> Dung lượng file nén: {dung_luong_nen} bytes")
print(f"-> Đã lưu dữ liệu mã hóa vào: {file_nen}\n")


print("--- (2) ĐỌC FILE SAU KHI GIẢM DUNG LƯỢNG & TRẢ VỀ ĐỊNH DẠNG BAN ĐẦU ---")

with open(file_nen, 'r', encoding='utf-8') as f:
    dong_du_lieu = f.readlines()
    
    tu_dien_da_luu = dong_du_lieu[0].strip('\n').split(',')
    vi_tri_da_luu = dong_du_lieu[1].split(' ')

van_ban_khoi_phuc = ""
for vt in vi_tri_da_luu:
    tu_goc = tu_dien_da_luu[int(vt)] 
    
    if tu_goc == '<XUONG_DONG>':
        van_ban_khoi_phuc += '\n'
    else:
        van_ban_khoi_phuc += tu_goc + " "

van_ban_khoi_phuc = van_ban_khoi_phuc.replace(" \n", "\n").strip()

print("Nội dung văn bản sau khi khôi phục:")
print("-" * 30)
print(van_ban_khoi_phuc)
print("-" * 30)