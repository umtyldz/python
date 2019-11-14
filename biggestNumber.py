# -*- coding: utf-8 -*-

sayi1 = int(input("İlk sayıyı girin:"))
sayi2 = int(input("İkinci sayıyı girin:"))
sayi3 = int(input("Üçüncü sayıyı girin:"))

enBuyuk = sayi1
#sayiConv = str(sayi)

if (sayi1>=sayi2) and (sayi1>=sayi3):
    enBuyuk = sayi1


elif (sayi2>=sayi1) and (sayi2>=sayi3):
    enBuyuk = sayi2
else:
    enBuyuk = sayi3

print("En Buyuk:" ,enBuyuk)
