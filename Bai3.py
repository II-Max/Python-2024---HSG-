def ktra(n):
          if(n < 2): return False
          for i in range(2, n):
                    if(n % i == 0):
                              return False
          return True
n = int(input("Nhập số n : "))
if(ktra(n)):
          print(n , " - là số nguyên tố")
else:
          print(n, " - không phải số nguyên tố")