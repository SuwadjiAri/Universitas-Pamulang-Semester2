a = int(input("Masukkan nilai A: "))
b = int(input("Masukkan nilai B: "))

def uts_no_satu(a, b) :    
    j = 0
    x = a
    if x <= b :
        if (x % 3) == 0 :
            print("kelipatan tiga", x)
            j = j + 1
            x = x + 1
            uts_no_satu(x, b)
        else :
            x = x + 1
            print("bukan kelipatan 3", x)
            uts_no_satu(x, b)
    else :
        print("x > b", j)
        
uts_no_satu(a, b)

