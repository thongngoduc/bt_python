import math
def Tinh(r):
    if r<0:
        print("Không hợp lệ")
    else:
        CV=2*math.pi*r
        DT=math.pi*r*r
        print("Chu vi là:",CV)
        print("Dien tich là:",DT)
r = int(input("Nhap vao ban kinh r:"))
Tinh(r)
