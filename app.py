import streamlit as st
from factorial import fact
import factorial as f
import pandas as pd

def main():
    st.title("Mô hình dự báo tỷ giá USD/VND")    
    # chia màn hình thành 2 cột
    col1, col2, col3 = st.columns(3)
    with col1:
        from_date = st.date_input("Chọn ngày bắt đầu")
        to_date = st.date_input("Chọn ngày kết thúc")
        loading_data_button = st.button("Tải dữ liệu")
    with col2:
        if loading_data_button:
            #tạo loading spinner khi tải dữ liệu
            with st.spinner("Đang tải dữ liệu..."):
                df = f.get_data(from_date, to_date)
                if df is not None:
                    # Hiển thị mô tả thống kê
                    st.write("Mô tả thống kê:")
                    st.write(df.describe())
    

    
                


if __name__ == "__main__":
    main()