def sumArray(n):
    if n == 1:
        return 1
    else:
        return n + sumArray(n-1)

def UCLN(a, b):
    if (b == 0):
        return a
    else:
        return UCLN(b, a % b)
    
n = int(input("Nhap so n: "))

# #* UCLN của hai số nguyên không thay đổi khi thay số lớn hơn bằng hiệu của nó với số nhỏ hơn
# #* Quá trình thay thế này được lặp đi lặp lại cho tới khi 2 số bằng nhau, khi đó UCLN chính là 1 trong 2 số.

# def ucln(a,b):
#     #* neu a hoac b bang 0 thi ucln la so con lai
#     if a == 0 | b == 0:
#         return a + b
#     while(a != b):
#         if a > b:
#             a -= b #* thay the so lon bang hieu hai so 
#         else:
#             b -= a #* thay the so nho bang hieu hai so
#     return a
    
a = int(input("Nhap so thu nhat: "))
b = int(input("Nhap so thu hai: "))

print("Tong day so tu 1 den", n, "la: ", sumArray(n))
print("Uoc chung lon nhat: ", UCLN(a, b))