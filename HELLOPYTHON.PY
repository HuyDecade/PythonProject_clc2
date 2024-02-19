def dem_tu_trong_caupho(cau_pho):
    # Chuyển đổi câu phố thành chữ thường để đảm bảo tính nhất quán
    cau_pho = cau_pho.lower()
    
    # Tách các từ trong câu phố
    tu_khoa = cau_pho.split()

    # Tạo một từ điển để lưu trữ số lần xuất hiện của từng từ
    dem_tu = {}

    # Đếm số lần xuất hiện của từng từ
    for tu in tu_khoa:
        # Lấy từng từ và loại bỏ các dấu câu
        tu = tu.strip(".,!?")

        # Tăng giá trị đếm cho từng từ trong từ điển
        dem_tu[tu] = dem_tu.get(tu, 0) + 1

    return dem_tu

# Ví dụ
cau_pho = "Nắng hồng ngoại qua mành lá xanh, Gió mát len lỏi từng hơi thở."
ket_qua = dem_tu_trong_caupho(cau_pho)

# Hiển thị kết quả
for tu, so_lan_xuat_hien in ket_qua.items():
    print(f"{tu}: {so_lan_xuat_hien} lần")
