from datetime import datetime, timedelta


thoi_gian_hien_tai = datetime.now()


thoi_gian_moi = thoi_gian_hien_tai + timedelta(seconds=5)

print("Thời gian hiện tại:", thoi_gian_hien_tai.strftime("%H:%M:%S"))
print("Thời gian sau khi thêm 5 giây:", thoi_gian_moi.strftime("%H:%M:%S"))