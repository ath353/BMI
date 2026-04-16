print("=" * 40)
print(f"{'MÁY TÍNH BMI  🏋️':^40}")
print("=" * 40)
print()

print("Vui lòng nhập thông tin: ")
ten_cua_ban = input("Tên của bạn là: ")
can_nang = float(input("Cân nặng của bạn là (kg): "))
chieu_cao = float(input("Chiều cao của bạn là (m): "))
tuoi = int(input("Tuổi của bạn: "))
gioi_tinh = input("Giới tính (nam/nu): ").strip().lower()


bmi = can_nang / (chieu_cao ** 2)
can_nang_min = 18.5 * (chieu_cao ** 2)
can_nang_max = 24.9 * (chieu_cao ** 2)


phan_loai = (
    "Thiếu cân" if bmi < 18.5 else
    "Bình thường" if bmi < 25 else
    "Thừa cân" if bmi < 30 else
    "Béo phì"
)


loi_khuyen = (
    "Cần tăng cân để khỏe mạnh hơn" if bmi < 18.5 else
    "Duy trì cân nặng hiện tại" if bmi < 25 else
    "Cần tập luyện và ăn uống hợp lý" if bmi < 30 else
    "Nên gặp bác sĩ để có chế độ phù hợp"
)


if gioi_tinh == "nam":
    phan_tram_mo = (1.20 * bmi) + (0.23 * tuoi) - 16.2
    phan_loai_mo = (
        "Quá thấp (nguy hiểm)" if phan_tram_mo < 6 else
        "Vận động viên"        if phan_tram_mo < 14 else
        "Săn chắc (Fit)"       if phan_tram_mo < 18 else
        "Bình thường"          if phan_tram_mo < 25 else
        "Béo phì"
    )
else:
    phan_tram_mo = (1.20 * bmi) + (0.23 * tuoi) - 5.4
    phan_loai_mo = (
        "Quá thấp (nguy hiểm)" if phan_tram_mo < 14 else
        "Vận động viên"        if phan_tram_mo < 21 else
        "Săn chắc (Fit)"       if phan_tram_mo < 25 else
        "Bình thường"          if phan_tram_mo < 32 else
        "Béo phì"
    )

print()
print("=" * 40)
print(f"{'KẾT QUẢ BMI':^40}")
print("=" * 40)
print(f"Họ tên         : {ten_cua_ban}")
print(f"Cân nặng       : {can_nang:.1f} kg")
print(f"Chiều cao      : {chieu_cao:.2f} m")
print(f"BMI            : {bmi:.2f}")
print(f"Phân loại      : {phan_loai}")
print("-" * 40)
print(f"% Mỡ cơ thể   : {phan_tram_mo:.1f} %")
print(f"Phân loại mỡ  : {phan_loai_mo}")
print("-" * 40)
print(f"Cân nặng lý tưởng: {can_nang_min:.1f} - {can_nang_max:.1f} kg")
print("-" * 40)
print(f"💡 Lời khuyên: {loi_khuyen}")
print("=" * 40)
print()
print("⚠️  Lưu ý: Kết quả chỉ mang tính tham khảo.")
print("   Hãy tham khảo bác sĩ để có đánh giá chính xác.")
