# 🏋️ Máy Tính BMI - Python ✅

## 1. Tên dự án
**Máy Tính BMI - Python**

## 2. Ứng dụng dự án
Đây là ứng dụng tính chỉ số BMI và phân tích tình trạng cơ thể, kèm tính toán % mỡ cơ thể và đưa ra lời khuyên phù hợp dựa trên kết quả.

### Tính năng chính
- 📊 Tính chỉ số BMI dựa trên cân nặng và chiều cao
- 🎯 Phân loại BMI theo chuẩn WHO (Thiếu cân / Bình thường / Thừa cân / Béo phì)
- 💪 Tính tỷ lệ % mỡ cơ thể theo giới tính và tuổi
- 📏 Tính cân nặng lý tưởng dựa trên chiều cao
- 💡 Đưa ra lời khuyên phù hợp với từng tình trạng

### 🎬 Demo
```
========================================
          MÁY TÍNH BMI 🏋️
========================================

Vui lòng nhập thông tin:
Tên của bạn là: Minh
Cân nặng (kg): 65
Chiều cao (m): 1.70
Tuổi: 25
Giới tính (nam/nu): nam

========================================
             KẾT QUẢ BMI
========================================
Họ tên         : Minh
Cân nặng       : 65.0 kg
Chiều cao      : 1.70 m
BMI            : 22.49
Phân loại      : Bình thường
----------------------------------------
% Mỡ cơ thể   : 16.9 %
Phân loại mỡ  : Săn chắc (Fit)
----------------------------------------
Cân nặng lý tưởng: 53.5 - 71.8 kg
----------------------------------------
💡 Lời khuyên: Duy trì cân nặng hiện tại
========================================

⚠️  Lưu ý: Kết quả chỉ mang tính tham khảo.
```

### 📐 Công thức sử dụng

**BMI:**
```
BMI = cân nặng (kg) / chiều cao² (m)
```

**% Mỡ cơ thể (ước lượng):**
```
% mỡ nam = 1.20 × BMI + 0.23 × tuổi - 16.2
% mỡ nữ  = 1.20 × BMI + 0.23 × tuổi - 5.4
```

**Phân loại BMI (WHO):**

| BMI | Phân loại |
|-----|-----------|
| < 18.5 | Thiếu cân |
| 18.5 - 24.9 | Bình thường ✅ |
| 25.0 - 29.9 | Thừa cân |
| ≥ 30.0 | Béo phì |

## 3. Công nghệ
- **Ngôn ngữ:** Python 3.x
- **Giao diện:** Command Line Interface (CLI)
- **Kiến thức áp dụng:**
  - `input()` + ép kiểu `float()`, `int()` — nhận dữ liệu từ người dùng
  - Toán tử số học — tính BMI, % mỡ, cân nặng lý tưởng
  - F-string + format số — hiển thị kết quả đẹp
  - Ternary expression — phân loại BMI và % mỡ

## 4. Hướng dẫn sử dụng

### Yêu cầu
- Đã cài đặt **Python 3.x** trên máy

### Các bước chạy chương trình
1. Mở terminal tại thư mục chứa project
2. Chạy lệnh:
   ```bash
   python main.py
   ```
3. Nhập thông tin theo yêu cầu: tên, cân nặng (kg), chiều cao (m), tuổi, giới tính
4. Xem kết quả BMI, % mỡ cơ thể, cân nặng lý tưởng và lời khuyên

> ⚠️ **Lưu ý:** Kết quả chỉ mang tính **tham khảo**. Vui lòng tham khảo ý kiến bác sĩ để có đánh giá chính xác.

## 5. Tác giả
- ath353
