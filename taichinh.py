def tinh_lai_kep(von_dau, lai_suat_nam, so_thang=12):
    """
    Hàm tính lãi kép theo tháng
    Công thức: A = P * (1 + r)^n
    """
    # Chuyển lãi suất năm (%) sang lãi suất tháng (thập phân)
    r_thang = (lai_suat_nam / 100) / 12
    
    # Tính tổng tiền nhận được
    tong_tien = von_dau * (1 + r_thang)**so_thang
    
    # Tính tiền lãi ròng
    tien_lai = tong_tien - von_dau
    
    return tong_tien, tien_lai

def main():
    print("--- CHƯƠNG TRÌNH TÍNH LỢI NHUẬN TIẾT KIỆM (12 THÁNG) ---")
    try:
        goc = float(input("Nhập số tiền gốc ban đầu (VNĐ): "))
        lai_suat = float(input("Nhập lãi suất hàng năm (%): "))
        
        tong, lai = tinh_lai_kep(goc, lai_suat)
        
        print("-" * 40)
        print(f"Số tiền gốc: {goc:,.0f} VNĐ")
        print(f"Lãi suất: {lai_suat}% / năm")
        print(f"Tổng tiền nhận được sau 1 năm: {tong:,.2f} VNĐ")
        print(f"Tiền lãi ròng: {lai:,.2f} VNĐ")
        print("-" * 40)
        
    except ValueError:
        print("Lỗi: Vui lòng nhập số tiền và lãi suất hợp lệ!")

if __name__ == "__main__":
    main()