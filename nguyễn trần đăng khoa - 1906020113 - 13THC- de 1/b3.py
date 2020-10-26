s = 0
n = int(input("moi ban nhap 1 so nguyen duong N: "))
while n <= 0:
    n = int(input("moi ban nhap lại: "))
for i in range(1,n + 1):
    if i == 13:
        break
    s +=i
print("s = ",s)