def ktra(n):
          if(n < 2): return False
          for i in range(2, n):
                    if(n % i == 0):
                              return False
          return True
n = int(input("Nhập số n : "))
p = 0
for i in range(2, 1000000):
          if(ktra(i)):
                    p += 1
                    print(i)
                    if(p == n):
                              break