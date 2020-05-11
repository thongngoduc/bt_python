def get_sum(*num):
    tmp = 0
    #duyet cac tham so
    for i in num:
        tmp += i
    return tmp
result = get_sum(1, 2, 3, 4, 5)
print(result)
(giải thích: trong Python cũng cấp cho chúng ta khai báo một\
 param đại diện cho các biến truyền vào hàm bằng cách thêm\
 dấu * vào trước param đó.)
