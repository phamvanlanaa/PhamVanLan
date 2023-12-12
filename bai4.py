import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if filepath:
        # Xử lý tệp đã chọn
        generate_report(filepath)

def generate_report(filepath):
    # Đọc dữ liệu từ tệp CSV
    data = pd.read_csv(filepath)

    # Phân tích dữ liệu và tạo biểu đồ
    # ...
    # Thêm mã xử lý của bạn ở đây để phân tích dữ liệu và tạo biểu đồ

    # Hiển thị biểu đồ
    plt.show()

# Tạo cửa sổ Tkinter
window = tk.Tk()

# Tạo nút "Chọn tệp"
open_button = tk.Button(window, text="Chọn tệp", command=open_file)
open_button.pack()

# Tạo nút "Tạo báo cáo"
create_button = tk.Button(window, text="Tạo báo cáo", command=generate_report)
create_button.pack()

# Chạy vòng lặp chính của ứng dụng
window.mainloop()import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt

def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if filepath:
        # Xử lý tệp đã chọn
        generate_report(filepath)

def generate_report(filepath):
    # Đọc dữ liệu từ tệp CSV
    data = pd.read_csv(filepath)

    # Phân tích dữ liệu và tạo biểu đồ
    # ...
    # Thêm mã xử lý của bạn ở đây để phân tích dữ liệu và tạo biểu đồ

    # Hiển thị biểu đồ
    plt.show()

# Tạo cửa sổ Tkinter
window = tk.Tk()

# Tạo nút "Chọn tệp"
open_button = tk.Button(window, text="Chọn tệp", command=open_file)
open_button.pack()

# Tạo nút "Tạo báo cáo"
create_button = tk.Button(window, text="Tạo báo cáo", command=generate_report)
create_button.pack()

# Chạy vòng lặp chính của ứng dụng
window.mainloop()