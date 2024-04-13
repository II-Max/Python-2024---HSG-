x = float(input("Nhập Số Thực x = "))
n = int(input("Nhập Số Nguyên n = "))
if(type(x) == float and type(n) == int):
          p = 1
          for i in range(1, n + 1):
                    print(p)
                    p += (i + 1) * (x ** i)
else:
          print("Nhập Sai Yêu Cầu, Hãy Nhập Lại.")
          x = float(input("Nhập Số Thực x = "))
          n = int(input("Nhập Số Nguyên n = "))