import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Sửa hiển thị trang toàn khung
    st.set_page_config(layout="wide")



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
    # Tính toán tỷ lệ hoàn thành, nếu Số cần nhập = 0 thì tỷ lệ hoàn thành = 0 để tránh chia cho 0
    df['Tỷ lệ hoàn thành'] = df.apply(lambda row: row['Tổng đã nhập'] / row['Số cần nhập'] * 100 if row['Số cần nhập'] > 0 else 0, axis=1)

    # Sắp xếp theo tổng đã nhập từ cao đến thấp
    df_sorted = df.sort_values('Tổng đã nhập', ascending=False).reset_index(drop=True)

    # Tạo biểu đồ bar ngang, với mỗi thanh bar hiên thị 3 phần: Đã nhập (cũ), Số mới nhập, Còn lại cần nhập
    # fig, ax = plt.subplots(figsize=(10, 8))
    # bar_width = 0.25
    # index = np.arange(len(df_sorted))
    # ax.bar(index, df_sorted['Đã nhập (cũ)'], bar_width, label='Đã nhập (cũ)')
    # ax.bar(index + bar_width, df_sorted['Số mới nhập'], bar_width, label='Số mới nhập')
    # ax.bar(index + 2 * bar_width, df_sorted['Còn lại cần nhập'], bar_width, label='Còn lại cần nhập')

    # ax.set_xlabel('Số lượng')
    # ax.set_ylabel('Tỉnh')
    # ax.set_title('Tình hình nhập theo tỉnh')
    # ax.legend()

    
    # Hiển thị 2 cột : cột bảng số liệu và cột biểu đồ
    #chỉnh sửa tỷ lệ cột hiển thị toàn bộ cột dữ liệu và 2 cột có chiều cao bằng nhau
    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("Bảng số liệu")
        # Hiển thị bảng số liệu với các cột : Tỉnh, Số cần nhập, Số mới nhập, Tổng đã nhập, Tỷ lệ hoàn thành. Chú ý cột tỷ lệ hoàn thành hiển thị dưới dạng phần trăm với 2 chữ số thập phân
        st.table(df_sorted[['Tỉnh', 'Số cần nhập', 'Số mới nhập', 'Tổng đã nhập', 'Tỷ lệ hoàn thành']].style.format({'Tỷ lệ hoàn thành': '{:.2f}%'.format}))
       
    with col2:
        st.subheader("Biểu đồ")
        # Tạo biểu đồ
        df_sorted = df_sorted.sort_values('Tổng đã nhập', ascending=False).reset_index(drop=True)

        # Tạo figure
        fig, ax = plt.subplots(figsize=(14, 12))
        y_pos = np.arange(len(df_sorted))

        # 2. Vẽ các phần của biểu đồ stacked
        ax.barh(y_pos, df_sorted['Đã nhập (cũ)'], 
                color='#2E86AB', label='Đã nhập (cũ)', edgecolor='white', linewidth=0.5)

        ax.barh(y_pos, df_sorted['Số mới nhập'], 
                left=df_sorted['Đã nhập (cũ)'],
                color='#06A77D', label='Số mới nhập', edgecolor='white', linewidth=0.5)

        ax.barh(y_pos, df_sorted['Còn lại cần nhập'], 
                left=df_sorted['Tổng đã nhập'],
                color='#F18F01', label='Còn lại cần nhập', edgecolor='white', linewidth=0.5)

        # 3. Tùy chỉnh trục và tiêu đề
        ax.set_yticks(y_pos)
        ax.set_yticklabels(df_sorted['Tỉnh'], fontsize=10)
        ax.invert_yaxis()  # Đảo ngược trục Y để tỉnh cao nhất nằm ở trên cùng
        ax.set_xlabel('Số lượng', fontsize=12, fontweight='bold')
        ax.set_title('Tình hình nhập theo tỉnh\n(Sắp xếp từ cao đến thấp theo tổng đã nhập)', 
                    fontsize=14, fontweight='bold', pad=20)

        # 4. Thêm giá trị thống kê NẰM NGOÀI thanh bar
        # Tính toán khoảng đệm (offset) dựa trên giá trị lớn nhất của cột 'Số cần nhập'
        max_val = df_sorted['Số cần nhập'].max()
        offset = max_val * 0.01  # Cách ra 1% so với giá trị lớn nhất

        for i, (idx, row) in enumerate(df_sorted.iterrows()):
            total_required = row['Số cần nhập']
            total_imported = row['Tổng đã nhập']
            percentage = (total_imported / total_required * 100) if total_required > 0 else 0
            
            # Tọa độ X: Lấy điểm kết thúc của thanh (Số cần nhập) cộng thêm một khoảng offset
            ax.text(total_required + offset, i, 
                    f"{int(total_imported)}/{int(total_required)} ({percentage:.0f}%)", 
                    va='center', 
                    ha='left', # Căn lề trái của chữ tại điểm tọa độ để chữ chạy sang phải
                    fontsize=9, 
                    fontweight='bold',
                    color='#333333')

        # Tăng giới hạn trục X một chút để chữ không bị tràn ra ngoài biên đồ thị
        ax.set_xlim(0, max_val * 1.15) 

        ax.grid(axis='x', alpha=0.3, linestyle='--')
        ax.legend(loc='upper right', frameon=True)
        plt.tight_layout()

        # Hiển thị trên Streamlit
        st.pyplot(fig)


    


if __name__ == "__main__":
    main()