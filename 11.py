import math

class TamGiac:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def chu_vi(self):
        return self.a + self.b + self.c

    def dien_tich(self):
        # Sử dụng công thức Heron để tính diện tích tam giác
        p = self.chu_vi() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

class TamGiacCan(TamGiac):
    def __init__(self, a, b):
        super().__init__(a, b, a)

class TamGiacVuong(TamGiac):
    def __init__(self, a, b):
        c = math.sqrt(a**2 + b**2)
        super().__init__(a, b, c)

class TamGiacDeu(TamGiacCan):
    def __init__(self, a):
        super().__init__(a, a)

    def dien_tich(self):
        return (math.sqrt(3) / 4) * self.a ** 2

# Ví dụ sử dụng:
tam_giac = TamGiac(3, 4, 5)
print(f"Chu vi tam giác: {tam_giac.chu_vi()}")
print(f"Diện tích tam giác: {tam_giac.dien_tich()}")

tam_giac_can = TamGiacCan(5, 6)
print(f"Chu vi tam giác cân: {tam_giac_can.chu_vi()}")
print(f"Diện tích tam giác cân: {tam_giac_can.dien_tich()}")

tam_giac_vuong = TamGiacVuong(3, 4)
print(f"Chu vi tam giác vuông: {tam_giac_vuong.chu_vi()}")
print(f"Diện tích tam giác vuông: {tam_giac_vuong.dien_tich()}")

tam_giac_deu = TamGiacDeu(4)
print(f"Chu vi tam giác đều: {tam_giac_deu.chu_vi()}")
print(f"Diện tích tam giác đều: {tam_giac_deu.dien_tich()}")
