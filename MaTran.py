def NT(n):
          if(n < 2):return False
          for i in range(2, n):
                    if(n % i == 0):
                              return False
          return True
A = []
dem = 0
n = int(input("Nhap SL Hang"))
m = int(input("Nhap SL Cot"))
for i in range(n):
          A1 = []
          for j in range(m):
                    A2 = int(input("Nhập phần tử tại hàng {} cột {}: ".format(i+1, j+1)))
                    A1.append(A2)
          A.append(A1)
for i in range(n):
          for j in range(m):
                    if(NT(A[i][j])): dem += 1
print(dem)