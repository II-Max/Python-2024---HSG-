k = int(input("Nhập số nguyên k = "))
A = []
dem1 = 0
dem2 = 0
while(1 == 1):
          x = int(input())
          A.append(x)
          if(x == 0):
                    break
for a in A:
          if(a > k):
                    dem1 += 1
          else: dem2 += 1
print("Các phần tử có GT lớn hơn k : ", dem1)
print("Các phần tử có GT nhỏ hơn k : ", dem2)