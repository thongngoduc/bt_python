class inhoa(object):
    def __init__(self, s):
        self.str1=s
    def hoa(self):
        return ''.join(s.upper())
s=input('Nhap chuoi:')
chuoi=inhoa(s)
print(chuoi.hoa())
