import math

class Diem:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def hien_thi(self):
        return f"({self.x}, {self.y})"

class Elip(Diem):
    def __init__(self, x, y, truc_lon, truc_nho):
        super().__init__(x, y)
        self.truc_lon = truc_lon
        self.truc_nho = truc_nho

    def dien_tich(self):
        return math.pi * self.truc_lon * self.truc_nho

class DuongTron(Elip):
    def __init__(self, x, y, ban_kinh):
        super().__init__(x, y, ban_kinh, ban_kinh)
        self.ban_kinh = ban_kinh

    def dien_tich(self):
        return math.pi * self.ban_kinh ** 2

# Ví dụ sử dụng:
diem = Diem(1, 2)
print(f"Tọa độ điểm: {diem.hien_thi()}")

elip = Elip(0, 0, 5, 3)
print(f"Tọa độ tâm elip: {elip.hien_thi()}")
print(f"Diện tích elip: {elip.dien_tich()}")

duong_tron = DuongTron(0, 0, 4)
print(f"Tọa độ tâm đường tròn: {duong_tron.hien_thi()}")
print(f"Diện tích đường tròn: {duong_tron.dien_tich()}")
