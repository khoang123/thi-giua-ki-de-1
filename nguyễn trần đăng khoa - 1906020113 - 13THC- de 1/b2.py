n = int(input("Nhập n:"))
def hien_thi_mua(n):
    if(1<=3 and n <=3):
        print("Mùa Xuân")
    elif(3<=6 and n <= 6):
        print("Mùa Hạ")
    elif (7<=9 and n <= 9):
        print("Mùa Thu")
    elif(9<=12 and n <= 12):
        print("Mùa Đông")
print("Nhập tháng: ",end="")
thang=int(input())
while thang<1 or thang>12:
    print("Tháng không hợp lệ vui lòng nhập lại!")
    thang=int(input("Nhap thang: "))
hien_thi_mua(n)   