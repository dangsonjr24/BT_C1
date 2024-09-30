class PhanSo:
    def __init__(self, tu_so, mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so

    def nhap_phan_so(self):
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số: "))
        while self.mau_so == 0:
            print("Mẫu số phải khác 0. Vui lòng nhập lại.")
            self.mau_so = int(input("Nhập mẫu số: "))

    def kiem_tra_hop_le(self):
        return self.mau_so != 0

    def in_phan_so(self):
        if self.kiem_tra_hop_le():
            print(f"Phân số: {self.tu_so}/{self.mau_so}")
        else:
            print("Phân số không hợp lệ.")

# Tạo một đối tượng PhanSo
phan_so = PhanSo(0, 1)
phan_so.nhap_phan_so()
phan_so.in_phan_so()
