import datetime

now = datetime.datetime.now()

print(f"Năm hiện tại: {now.strftime('%Y')}")
print(f"Tháng hiện tại bằng chữ: {now.strftime('%B')}")
print(f"Tuần hiện tại là tuần thứ mấy trong năm: {now.strftime('%W')}")

first_day_of_month = now.replace(day=1)
first_week_of_year = int(first_day_of_month.strftime('%W'))
current_week_of_year = int(now.strftime('%W'))
week_of_month = current_week_of_year - first_week_of_year + 1
print(f"Tuần hiện tại là tuần thứ mấy trong tháng: {week_of_month}")

print(f"Ngày hiện tại là ngày thứ mấy trong năm: {now.strftime('%j')}")
print(f"Ngày dương lịch hiện tại là ngày: {now.strftime('%d')}")
print(f"Thứ của ngày hiện tại: {now.strftime('%A')}")
print(f"Giờ phút giây hiện tại: {now.strftime('%H:%M:%S')}")