#VD : Nhập a,b in ra UCLN, BCNL
def UCLN(u, v):
          l = 0
          while(v != 0):
                    l = u % v
                    u = v
                    v = l
          return u
a = int(input("Nhập số nguyên a : "))
b = int(input("Nhập số nguyên b : "))
print("Ước chung lớn nhất của a và b : ",UCLN(a, b))
print("Bội chung lớn nhất của a và b : ",(a * b)/UCLN(a, b))