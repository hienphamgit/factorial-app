import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from arch import arch_model
import warnings

warnings.filterwarnings("ignore")

def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

# --- 1. Thu thập dữ liệu ---
# Sử dụng yfinance để tải dữ liệu USD/VND (sử dụng mã cặp tiền VND=X)
def get_data(from_date, to_date):
    from_date_string = from_date.strftime('%Y-%m-%d')
    to_date_string = to_date.strftime('%Y-%m-%d')
    try:
        data = yf.download("VND=X", start=from_date_string, end=to_date_string)
    except Exception as e:
        print(f"Lỗi khi tải dữ liệu: {e}")
        return None
    if data.empty:
        print("Không có dữ liệu trong khoảng thời gian đã chọn.")
        return None
    data = data[['Close']].rename(columns={'Close': 'USD_VND'})
    df = pd.DataFrame(data) # Gán MultiIndex vào cột
    df.columns = df.columns.droplevel(1) # Loại bỏ cấp độ thứ 2 (VND=X)
    return df