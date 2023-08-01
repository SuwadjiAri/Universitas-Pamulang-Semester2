a=float(input("masukkan nilai a:"))
b=float(input("masukkan nilai b:"))
c=float(input("masukkan nilai c:"))

if (a+b>c) and (a+c>b) and (b+c>a):
    print("segitiga dapat dibuat")
    if (a==b) and (a==c) and (b==c):
        print("segitiga sama sisi")
    elif (a==b) or (a==c) or (b==c):
        print("segitiga sama kaki")
    else:
        print("segitiga sembarang")
else:
    print("segitiga tidak dapat dibuat")