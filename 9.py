import math

class DaGiac:
    def __init__(self, cac_canh):
        self.cac_canh = cac_canh

    def chu_vi(self):
        return sum(self.cac_canh)

class HinhBinhHanh(DaGiac):
    def __init__(self, day, canh, chieu_cao):
        super().__init__([day, canh, day, canh])
        self.day = day
        self.canh = canh
        self.chieu_cao = chieu_cao

    def dien_tich(self):
        return self.day * self.chieu_cao

class HinhChuNhat(HinhBinhHanh):
    def __init__(self, chieu_rong, chieu_dai):
        super().__init__(chieu_rong, chieu_dai, chieu_dai)
        self.chieu_rong = chieu_rong
        self.chieu_dai = chieu_dai

    def dien_tich(self):
        return self.chieu_rong * self.chieu_dai

class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)
        self.canh = canh

    def dien_tich(self):
        return self.canh ** 2

# Ví dụ sử dụng:
da_giac = DaGiac([3, 4, 5])
print(f"Chu vi đa giác: {da_giac.chu_vi()}")

hinh_binh_hanh = HinhBinhHanh(5, 3, 4)
print(f"Chu vi hình bình hành: {hinh_binh_hanh.chu_vi()}")
print(f"Diện tích hình bình hành: {hinh_binh_hanh.dien_tich()}")

hinh_chu_nhat = HinhChuNhat(4, 6)
print(f"Chu vi hình chữ nhật: {hinh_chu_nhat.chu_vi()}")
print(f"Diện tích hình chữ nhật: {hinh_chu_nhat.dien_tich()}")

hinh_vuong = HinhVuong(4)
print(f"Chu vi hình vuông: {hinh_vuong.chu_vi()}")
print(f"Diện tích hình vuông: {hinh_vuong.dien_tich()}")
