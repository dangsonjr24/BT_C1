class Stack:
    def __init__(self, suc_chua):
        self.capacity = suc_chua
        self.stack = []
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self):
        return len(self.stack) == self.capacity
    
    def push(self, phan_tu):
        if self.is_full():
            print("Ngăn xếp đã đầy. Không thể đẩy phần tử vào.")
        else:
            self.stack.append(phan_tu)
    
    def pop(self):
        if self.is_empty():
            print("Ngăn xếp trống. Không thể lấy phần tử ra.")
        else:
            return self.stack.pop()
    
    def count(self):
        return len(self.stack)
    
    def hien_thi(self):
        print("Ngăn xếp:", self.stack)

# Ví dụ sử dụng
suc_chua = int(input("Nhập sức chứa của ngăn xếp: "))
ngan_xep = Stack(suc_chua)

while True:
    print("\n1. Đẩy vào\n2. Lấy ra\n3. Hiển thị\n4. Đếm số phần tử\n5. Thoát")
    lua_chon = int(input("Nhập lựa chọn của bạn: "))
    
    if lua_chon == 1:
        phan_tu = float(input("Nhập phần tử để đẩy vào: "))
        ngan_xep.push(phan_tu)
    elif lua_chon == 2:
        print("Phần tử lấy ra:", ngan_xep.pop())
    elif lua_chon == 3:
        ngan_xep.hien_thi()
    elif lua_chon == 4:
        print("Số phần tử trong ngăn xếp:", ngan_xep.count())
    elif lua_chon == 5:
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
