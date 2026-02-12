import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    st.title("Cập nhật tình hình nhập liệu trên nền tảng")    

    #tạo mục lớn "1. Tình hình nhập theo tỉnh"
    st.header("1. Tình hình nhập theo tỉnh")

    # Nhập dữ liệu từ bảng
    data_tintoipham = {
        'Tỉnh': ['An Giang', 'Bắc Ninh', 'Cà Mau', 'Cao Bằng', 'Cần Thơ', 'Đà Nẵng', 
                'Đắk Lắk', 'Điện Biên', 'Đồng Nai', 'Đồng Tháp', 'Gia Lai', 'Hà Nội',
                'Hà Tĩnh', 'Hải Phòng', 'Hồ Chí Minh', 'Hưng Yên', 'Khánh Hòa', 'Kiên Giang',
                'Lạng Sơn', 'Lào Cai', 'Lâm Đồng', 'Nghệ An', 'Ninh Bình', 'Phú Thọ',
                'Quảng Ngãi', 'Quảng Ninh', 'Quảng Trị', 'Sơn La', 'Tây Ninh', 'Thái Nguyên',
                'Thanh Hóa', 'Huế', 'Tuyên Quang', 'Vĩnh Long'],
        'Số cần nhập': [426, 378, 188, 473, 80, 430, 182, 66, 457, 222, 287, 2367, 121, 504,
                        53, 154, 355, 47, 365, 38, 147, 291, 363, 261, 166, 1951, 125, 80, 
                        173, 235, 120, 86, 120, 173],
        'Số mới nhập': [12, 0, 0, 0, 12, 99, 0, 3, 39, 0, 0, 103, 1, 1, 38, 0, 0, 11, 0, 0,
                        0, 3, 1, 0, 4, 0, 1, 0, 0, 2, 31, 15, 1, 0],
        'Tổng đã nhập': [201, 99, 99, 93, 227, 721, 149, 61, 457, 84, 193, 1099, 7, 170, 410,
                        135, 265, 381, 66, 164, 176, 104, 116, 88, 164, 1979, 141, 63, 427,
                        53, 637, 286, 75, 192]
    }

    df = pd.DataFrame(data_tintoipham)
    # Tính toán các thành phần
    df['Đã nhập (cũ)'] = df['Tổng đã nhập'] - df['Số mới nhập']
    df['Còn lại cần nhập'] =  df['Số cần nhập'] - df['Tổng đã nhập']
    #còn lại cần nhập 0 nếu đã nhập đủ hoặc vượt quá số cần nhập
    df['Còn lại cần nhập'] = df['Còn lại cần nhập'].apply(lambda x: 0 if x < 0 else x)
    # Sắp xếp theo tổng đã nhập từ cao đến thấp
    df_sorted = df.sort_values('Tổng đã nhập', ascending=True)
    
    # Tạo 2 cột hiển thị, một cột là số liệu bảng, một cột là biểu đồ
    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("Bảng số liệu")
        st.dataframe(df_sorted.reset_index(drop=True))
    with col2:
        st.subheader("Biểu đồ số liệu")
        # Tạo biểu đồ thanh chồng
        bar_width = 0.4
        index = np.arange(len(df_sorted))
        plt.figure(figsize=(10, 8))
        plt.barh(index, df_sorted['Đã nhập (cũ)'], bar_width, label='Đã nhập (cũ)', color='skyblue')
        plt.barh(index, df_sorted['Số mới nhập'], bar_width, left=df_sorted['Đã nhập (cũ)'], label='Số mới nhập', color='lightgreen')
        plt.barh(index, df_sorted['Còn lại cần nhập'], bar_width, left=df_sorted['Đã nhập (cũ)'] + df_sorted['Số mới nhập'], label='Còn lại cần nhập', color='lightcoral')
        plt.yticks(index, df_sorted['Tỉnh'])
        plt.xlabel('Số liệu')
        plt.title('Biểu đồ số liệu')
        plt.legend()
        st.pyplot(plt)


if __name__ == "__main__":
    main()