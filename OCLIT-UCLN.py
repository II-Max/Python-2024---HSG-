#VD : Nhập a,b in ra UCLN
def UCLN(u, v):
          l = 0
          while(v != 0):
                    l = u % v
                    u = v
                    v = l
          return u
a = int(input("Nhập số nguyên a : "))
b = int(input("Nhập số nguyên b : "))
print(UCLN(a, b))