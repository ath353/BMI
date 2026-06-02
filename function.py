print("=== Chương trình tính BMI viết bằng hàm ===")
def tinh_bmi(can_nang, chieu_cao):
    bmi = can_nang / (chieu_cao**2)
    return round(bmi,2)

def phan_loai_bmi(bmi):
    if bmi < 18.5:
        return "Thiếu cân"
    elif bmi < 25:
        return "Bình thường"
    elif bmi < 30:
        return "Thừa cân"
    else:
        return "Béo phì"

def tinh_mo(bmi, tuoi, gioi_tinh):
    if gioi_tinh == "nam":
        phan_tram_mo = (1.20 * bmi) + (0.23 * tuoi) - 16.2
    else:
        phan_tram_mo = (1.20 * bmi) + (0.23 * tuoi) - 5.4
    return phan_tram_mo

def phan_loai_mo(phan_tram_mo, gioi_tinh):
    if gioi_tinh == "nam":
        if phan_tram_mo < 6:
            return  "Quá thấp (Nguy hiểm)"
        elif phan_tram_mo < 14:
            return "Vận động viên"
        elif phan_tram_mo < 18:
            return  "Săn chắc (Fit)"
        elif phan_tram_mo < 25:
            return  "Bình thường"
        else:
            return "Béo phì"
    elif gioi_tinh == "nữ":
        if phan_tram_mo < 14:
            return "Quá thấp (Nguy hiểm)"
        elif phan_tram_mo < 21:
            return  "Vận động viên"
        elif phan_tram_mo < 25:
            return  "Săn chắc (Fit)"
        elif phan_tram_mo < 32:
            return "Bình thường"
        else:
            return "Béo phì"
    else:
        return "Giới tính không hợp lý!"

def in_ket_qua(ten, can_nang, chieu_cao, bmi, phan_loai, phan_tram_mo, kq_mo):
    print()
    print("="*40)
    print(f"{'KẾT QUẢ BMI':^40}")
    print(f"Họ tên: {ten}")
    print(f"Cân nặng: {can_nang}")
    print(f"Chiều cao: {chieu_cao}")
    print(f"BMI = {bmi}")
    print(f"Phân loại {phan_loai}")
    print("-"*40)
    print(f"% Mỡ cơ thể: {phan_tram_mo:.1f}%")
    print(f"Phân loại mỡ: {kq_mo}")

ten = input("Mời nhập tên: ")
can_nang = float(input("Mời nhập cân nặng: "))
chieu_cao = float(input("Mời nhập chiều cao: "))
tuoi = int(input("Mời nhập tuổi: "))
gioi_tinh = input("Nhập giới tính: ").strip().lower()

bmi = tinh_bmi(can_nang, chieu_cao)
phan_loai = phan_loai_bmi(bmi)
phan_tram_mo = tinh_mo(bmi, tuoi, gioi_tinh)
kq_mo= phan_loai_mo(phan_tram_mo, gioi_tinh)
in_ket_qua(ten, can_nang, chieu_cao, bmi, phan_loai, phan_tram_mo, kq_mo)
