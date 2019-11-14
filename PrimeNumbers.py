# -*- coding: utf-8 -*-
import time
import random
start_time = time.time()



asal=0
verilensayi=int(random.uniform(30,70))
#verilensayi = 1500

bulunan=0 #kac tane bulundu diye
asalsayilar="" #ensonda listelerken


for herbirsayi in range(2,verilensayi):
    asalMi=True #baştan asal diyoruz, altta kontrol ediyoruz
    
    #WHILE
    sayac=2 #2den başlayarak sayıyı böler mi kontrol ediyoruz
    while sayac < herbirsayi:
        
        if herbirsayi % sayac == 0: #tam bolunuyorsa asal degildir
            asalMi = False
            
        sayac=sayac+1 #bir sonraki sayıyla bölmeyi denemek için
        
    #WHILE BİTTİ, kendinden küçük hepsine böldük,
    
    # arada tam bölen çıkmadıysa  asalMI=True kalmıştır
    

    if asalMi:
        #başta yada sonda virgül olmasın
        virgul=","
        if bulunan==0:
            virgul=""
        #başta yada sonda virgül olmasın
        
        bulunan=bulunan+1 #kaç tane bulduğumuzu sayıyoruz
        asalsayilar = asalsayilar + virgul + str(herbirsayi)
        




    if bulunan > 9999:  # Hızlı test
        break

sure=str(round((time.time() - start_time), 5))  #virgulden sonraki basamak sayısı azaltmak için "round"

print(sure +" sürede, toplam " + str(bulunan)+ " adet asal sayı: " + asalsayilar)
