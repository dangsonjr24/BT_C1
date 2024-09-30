class ThiSinh:
    def __init__(self, ho_ten, diem_toan, diem_ly, diem_hoa):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def nhap_thong_tin(self):
        self.ho_ten = input("Nhập họ tên thí sinh: ")
        self.diem_toan = float(input("Nhập điểm Toán: "))
        self.diem_ly = float(input("Nhập điểm Lý: "))
        self.diem_hoa = float(input("Nhập điểm Hóa: "))

    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

    def in_thong_tin(self):
        print(f"Họ tên: {self.ho_ten}")
        print(f"Điểm Toán: {self.diem_toan}")
        print(f"Điểm Lý: {self.diem_ly}")
        print(f"Điểm Hóa: {self.diem_hoa}")
        print(f"Tổng điểm: {self.tinh_tong_diem()}")

# Tạo danh sách thí sinh
danh_sach_thi_sinh = []

# Nhập thông tin thí sinh
so_luong_thi_sinh = int(input("Nhập số lượng thí sinh: "))
for _ in range(so_luong_thi_sinh):
    thi_sinh = ThiSinh("", 0, 0, 0)
    thi_sinh.nhap_thong_tin()
    danh_sach_thi_sinh.append(thi_sinh)

# In danh sách thí sinh trúng tuyển
diem_chuan = 20
thi_sinh_trung_tuyen = [ts for ts in danh_sach_thi_sinh if ts.tinh_tong_diem() >= diem_chuan]
thi_sinh_trung_tuyen.sort(key=lambda ts: ts.tinh_tong_diem(), reverse=True)

print("\nDanh sách thí sinh trúng tuyển:")
for ts in thi_sinh_trung_tuyen:
    ts.in_thong_tin()
