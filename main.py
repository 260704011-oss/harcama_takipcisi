y = 0
adet = 0 
while True:
    try:
        x = float(input("Ne kadar harcayacaksınız? (Bitirmek için 0): "))
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")
        continue

    if x == 0:
        break
    if x < 0:
        print("Lütfen geçerli bir miktar giriniz.")
        continue
    y += x
    adet += 1

if adet > 0:
    print("Harcama adetiniz:", adet)
    print("Toplam harcamanız:", y, "TL")
else:
    print("Hiç harcama yapmadınız.")
