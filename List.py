#VD : Nhập vào một danh sách A có n phần tử, đứa
n = input()
A = list(map(int, n.split()))
B = []
C = []
D = []
demsoduong = 0
for a in A:
          if(a % 2 != 0):
                    B.append(a)
          if(a % 2 == 0):
                    C.append(a)
          if(a > 0):
                    D.append(a)
print("Các số lẻ trong mảng : ")
for b in B:
          print(" - ",b)
print("Số lượng phần tử lẻ trong mảng b là : ", len(B))
print("Số lượng các phần tử chăn trong dãy là : ", len(C))
print("Số lượng các phần tử dương trong dãy là : ", len(D))
print("Tổng các số chẵn : ", sum(C))