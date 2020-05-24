class Cricle(object):
    def __init__(self,r):
        self.radius=r
    def area(self):
        return self.radius**2*3.14
    def perimeter(self):
        return self.radius*2*3.14
r=int(input("Nhap ban kinh:"))
aCircle=Cricle(r)
print("Dien tich hinh tron la:",aCircle.area())
print('Chu vi hinh tron la:',aCircle.perimeter())
