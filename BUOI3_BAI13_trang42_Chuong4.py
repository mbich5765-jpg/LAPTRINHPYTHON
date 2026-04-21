def chuan_hoa_chuoi(s):
 
    lines = s.splitlines()
    
    formatted_lines = []
    for line in lines:
       
        cleaned_line = " ".join(line.split())
        
      
        cleaned_line = cleaned_line.replace(" .", ".").replace(" ,", ",")
        
       
        formatted_lines.append(cleaned_line)
   
    return "\n".join(formatted_lines)


chuoi_chua_hoan_chinh = """    Quê  hương
Quê hương là   chùm khế   ngọt.
   Cho con trèo hái   mỗi  ngày  .
Quê  hương là   đường  đi học .
  Con về  rợp bướm  vàng bay .
  Đỗ    Trung Quân    """


chuoi_hoan_chinh = chuan_hoa_chuoi(chuoi_chua_hoan_chinh)

print("--- Kết quả sau khi chuẩn hóa ---")
print(chuoi_hoan_chinh)