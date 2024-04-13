from itertools import count
import sys
from tkinter import N
sys.stdin = open("HS.inp", "r")
sys.stdout = open("HS.out", "w")
#f = open("HS.inp", "r")
def tachho(a):
          luu = ""
          for i in range(len(a)):
                    if(a[i] == " "):
                              break
                    else:
                              luu += a[i]
          return luu
def SX(a):
          for i in range(1, len(a) -1, 2):
                    for j in range(1, len(a) - 2, 2):
                              if(a[j] > a[j + 2]):
                                        a[j], a[j + 2] = a[j + 2], a[j] #Đổi số
                                        a[j - 1],a[j + 1] = a[j + 1], a[j - 1] #Đổi tên
          return a
n = int(input("Nhap So Luong Hoc Sinh : "))
A = []
H = []
Hs = []
for i in range(n):
          a = input()
          A.append(a)
          b = int(input())
          A.append(b)
print("Day Trc Khi Duoc SX : ")
print(A)
A = SX(A)
print("Day Sau Khi Duoc SX : ")
print(A)
for i in range(0,len(A), 2): #Tách các họ ra 1 mảng khác
          H.append(tachho(A[i]))
for i in range(len(H)): #Thêm số lượng
          Hs.append(H.count(H[i]))
for i in range(len(H)):
          print("Ho ", H[i], " Xuat Hien ", Hs[i], " Lan")