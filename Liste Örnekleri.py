import time

print("""
______________________________________________________________________________________

Birinci Liste : ["yazıcı", "klavye", "işlemci", "bellek", "sabit disk"]

İkinci Liste : ["işletim sistemi", "web tarayıcı"]
______________________________________________________________________________________

-Birinci listeyi görmek için "birinci" yazın.
-İkinci listeyi görmek için "ikinci" yazın.

-Birinci listeyi baştaki içeriğe geri döndürmek istiyorsanız "clear1" yazın.
-İkinci listeyi baştaki içeriğe geri döndürmek istiyorsanız "clear2" yazın.

1. Append1 Birinci Liste (Listenin sonuna istediğiniz bir şey ekleyin.)

2. Append2 İkinci Liste (Listenin sonuna istediğiniz bir şey ekleyin.)

3. Extend1 (Birinci liste ile ikinci listeyi birleştirme.)

4. Extend2 (İkinci liste ile birinci listeyi birleştirme.)

5. Insert1 Birinci liste (Listenin istediğiniz bir yerine, istediğiniz bir şey ekleyin.)

6. Insert2 İkinci liste (Listenin istediğiniz bir yerine, istediğiniz bir şey ekleyin.)

7. Remove1 Birinci liste (Listenin içindeki istediğiniz bir elemanı silmek için kullanın.)

8. Remove2 İkinci liste (Listenin içindeki istediğiniz bir elemanı silmek için kullanın.)

İşlemleri görmek için 'işlemler' yazın.
Çıkmak için 'q' ya basın.
""")

birinci_liste=["yazıcı", "klavye", "işlemci", "bellek", "sabit disk"]
ikinci_liste=["işletim sistemi", "web tarayıcı"]

while True:
    islem = input("İşlemi seçiniz :")

    if islem == "q":
        print("Program sonlandırılıyor...")
        break
    elif islem == "birinci":
        print("Birinci listenin son hali :",birinci_liste)
    
    elif islem == "ikinci":
        print("İkinci listenin son hali :",ikinci_liste)

    elif islem == "1":
        _ek = input("Birinci listenin sonuna eklemek istediğiniz şeyi yazınız :")
        birinci_liste.append(_ek)
        print("Listenin son hali :",birinci_liste)

    elif islem == "2":
        _ek2 = input("İkinci listenin sonuna eklemek istediğiniz şeyi yazınız :")
        ikinci_liste.append(_ek2)
        print("Listenin son hali :",ikinci_liste)

    elif islem == "3":
        print("Birinci listenin içi :",birinci_liste)
        time.sleep(2)
        print("İkinci listenin içi :",ikinci_liste)
        time.sleep(2)
        birinci_liste.extend(ikinci_liste)
        print("Birinci listenin son hali :",birinci_liste)

    elif islem == "4":
        print("Birinci listenin içi :",birinci_liste)
        time.sleep(2)
        print("İkinci listenin içi :",ikinci_liste)
        time.sleep(2)
        ikinci_liste.extend(birinci_liste)
        print("İkinci listenin son hali :",ikinci_liste)  

    elif islem == "5":
        kel_ = input("Birinci listeye eklemek istediğiniz kelimeyi yazınız :")
        sira_ = int(input("Birinci listeye eklemek istediğiniz kelimenin kaçıncı sırada olacağını yazınız :"))
        sira_ = (sira_ - 1)
        birinci_liste.insert(sira_, kel_)
        print("Birinci listenin son hali :",birinci_liste)

    elif islem == "6":
        _kel = input("İkinci listeye eklemek istediğiniz kelimeyi yazınız :")
        _sira = int(input("İkinci listeye eklemek istediğiniz kelimenin kaçıncı sırada olcağını yazınız :"))
        _sira = (_sira - 1)
        ikinci_liste.insert(_sira, _kel)
        print("İkinci listenin son hali :",ikinci_liste)    

    elif islem == "7":
        print("Birinci listenin son hali :",birinci_liste)
        time.sleep(1)
        sil_ = input("Listenin içinden silmek istediğiniz elemanı hatasız yazınız :")
        birinci_liste.remove(sil_)
        print("Birinci listenin son hali :",birinci_liste)

    elif islem == "8":
        print("İkinci listenin son hali :",ikinci_liste)
        time.sleep(1)
        _sil = input("Listenin içinden silmek istediğiniz elemanı hatasız yazınız :")
        ikinci_liste.remove(_sil)
        print("İkinci listenin son hali :",ikinci_liste)

    elif islem == "clear1":
        print("Birinci listenin şu anki hali :",birinci_liste)
        print("Birinci liste en baştaki haline döndürülüyor...")
        time.sleep(3)
        birinci_liste=["yazıcı", "klavye", "işlemci", "bellek", "sabit disk"]
        print("Birinci listenin şu anki hali :",birinci_liste)

    elif islem == "clear2": 
        print("İkinci listenin şu anki hali :",ikinci_liste)
        print("İkinci liste en baştkai haline döndürülüyor...")
        time.sleep(3)
        ikinci_liste=["işletim sistemi", "web tarayıcı"]
        print("İkinci listenin şu anki hali :",ikinci_liste)

    elif islem == "işlemler" or "islem":
        print("""
______________________________________________________________________________________

Birinci Liste : ["yazıcı", "klavye", "işlemci", "bellek", "sabit disk"]

İkinci Liste : ["işletim sistemi", "web tarayıcı"]
______________________________________________________________________________________

-Birinci listeyi görmek için "birinci" yazın.
-İkinci listeyi görmek için "ikinci" yazın.

-Birinci listeyi baştaki içeriğe geri döndürmek istiyorsanız "clear1" yazın.
-İkinci listeyi baştaki içeriğe geri döndürmek istiyorsanız "clear2" yazın.

1. Append1 Birinci Liste (Listenin sonuna istediğiniz bir şey ekleyin)

2. Append2 İkinci Liste (Listenin sonuna istediğiniz bir şey ekleyin)

3. Extend1 (Birinci liste ile ikinci listeyi birleştirme)

4. Extend2 (İkinci liste ile birinci listeyi birleştirme)

5. Insert1 Birinci liste (Listenin istediğiniz bir yerine, istediğiniz bir şey ekleyin)

6. Insert2 İkinci liste (Listenin istediğiniz bir yerine, istediğiniz bir şey ekleyin)

7. Remove1 Birinci liste (Listenin içindeki istediğiniz bir elemanı silmek için kullanın.)

8. Remove2 İkinci liste (Listenin içindeki istediğiniz bir elemanı silmek için kullanın.)

İşlemleri görmek için 'işlemler' yazın.
Çıkmak için 'q' ya basın.
        """)
    
    else:
        print("Böyle bir işlem bulunmamakta...")
        time.sleep(2)
