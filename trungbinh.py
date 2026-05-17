def tinh_trung_binh(danh_sach_diem):
    """Hàm tính trung bình cộng của một danh sách số"""
    if not danh_sach_diem:
        return 0
    return sum(danh_sach_diem) / len(danh_sach_diem)

def xep_loai(diem_tb):
    """Hàm xếp loại dựa trên điểm trung bình"""
    if diem_tb >= 8.0:
        return "Giỏi"
    elif diem_tb >= 6.5:
        return "Khá"
    elif diem_tb >= 5.0:
        return "Trung bình"
    else:
        return "Yếu/Kém"

def main():
    print("--- CHƯƠNG TRÌNH QUẢN LÝ ĐIỂM SINH VIÊN ---")
    try:
        # Nhập dữ liệu: ví dụ 8, 7.5, 9, 10
        nhap = input("Nhập danh sách điểm (cách nhau bởi dấu phẩy): ")
        
        # Chuyển chuỗi nhập vào thành danh sách số thực (float)
        diem_so = [float(x.strip()) for x in nhap.split(",")]
        
        # Tính toán
        tb = tinh_trung_binh(diem_so)
        loai = xep_loai(tb)
        
        # Xuất kết quả
        print("-" * 30)
        print(f"Số môn đã học: {len(diem_so)}")
        print(f"Điểm trung bình: {tb:.2f}")
        print(f"Xếp loại học lực: {loai}")
        print("-" * 30)
        
    except ValueError:
        print("Lỗi: Vui lòng chỉ nhập số và dùng dấu phẩy để ngăn cách!")

if __name__ == "__main__":
    main()