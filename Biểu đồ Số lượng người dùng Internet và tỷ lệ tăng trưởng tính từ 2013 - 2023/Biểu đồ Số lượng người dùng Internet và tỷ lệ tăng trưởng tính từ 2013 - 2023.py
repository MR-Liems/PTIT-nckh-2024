import matplotlib.pyplot as plt
import numpy as np

# Adjust the years to the new format "1/2013" instead of "Jan 2013"
new_labels = ['1/2013', '1/2014', '1/2015', '1/2016', '1/2017', '1/2018', '1/2019', '1/2020', '1/2021', '1/2022', '1/2023']

# Dữ liệu số người dùng Internet theo từng năm (giả sử là hàng triệu người dùng)
users = [34.6, 37.2, 41.3, 49.1, 54.4, 66.0, 65.5, 67.6, 72.1, 72.6, 77.9]

# Dữ liệu tỷ lệ tăng trưởng qua các năm
growth_rates = [7.6, 10.9, 19.0, 8.0, 21.3, -0.7, 3.2, 6.5, 0.8, 7.3]

# Tính toán vị trí của các cột và các điểm trên đường biểu đồ
x_positions = np.arange(len(new_labels))  # Vị trí các cột trên trục x
line_positions = x_positions[:-1] + 0.5  # Vị trí của các điểm trên đường (giữa các cột)

# Tạo biểu đồ và vẽ cột
fig, ax1 = plt.subplots(figsize=(10, 6))

# Vẽ biểu đồ cột cho số lượng người dùng
bars = ax1.bar(x_positions, users, color='skyblue', label='Internet Users (in millions)', tick_label=new_labels)

# Thêm các số liệu vào trên các cột
for bar, user_count in zip(bars, users):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, height, f'{user_count}M', ha='center', va='bottom', color='black')

# Gắn nhãn trục
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Internet Users (in millions)', fontsize=12)

# Vẽ đường biểu đồ cho tỷ lệ tăng trưởng
ax2 = ax1.twinx()
ax2.plot(line_positions, growth_rates, color='red', marker='o', linestyle='-', linewidth=2, label='Growth Rate (%)')

# Thêm các tỷ lệ tăng trưởng vào biểu đồ đường
for i, rate in enumerate(growth_rates):
    ax2.text(line_positions[i], rate + 0.3, f'{rate}%', ha='center', va='bottom', color='red')

# Gắn nhãn cho trục y của tỷ lệ tăng trưởng
ax2.set_ylabel('Growth Rate (%)', fontsize=12)

# Thêm chú thích cho cả biểu đồ cột và biểu đồ đường
ax1.legend(loc='upper left', bbox_to_anchor=(0.05, 1.05), fontsize=10)
ax2.legend(loc='upper right', bbox_to_anchor=(0.95, 1.05), fontsize=10)

# Đặt tiêu đề và căn chỉnh
plt.title('Internet Users and Growth Rate in Vietnam (2013-2023)', fontsize=14, pad=30)

# Xoay nhãn trục x để tránh bị chồng
plt.xticks(rotation=45, ha='right')

# Căn chỉnh tổng thể biểu đồ
fig.tight_layout()

# Hiển thị biểu đồ
plt.show()
