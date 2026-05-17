def tinh_giai_thua(n):
    """Hàm tính giai thừa bằng vòng lặp for"""
    ket_qua = 1
    if n < 0:
        return "Không xác định (n phải >= 0)"
    elif n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            ket_qua *= i
        return ket_qua

def main():
    print("--- CHƯƠNG TRÌNH TÍNH SỐ CÁCH XẾP HÀNG (GIAI THỪA) ---")
    try:
        n = int(input("Nhập số lượng người (n): "))
        
        # Gọi hàm tính toán
        ket_qua = tinh_giai_thua(n)
        
        # Hiển thị kết quả
        if isinstance(ket_qua, int):
            print(f"Số cách sắp xếp cho {n} người là: {ket_qua} cách.")
        else:
            print(ket_qua)
            
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nguyên hợp lệ!")

if __name__ == "__main__":
    main()