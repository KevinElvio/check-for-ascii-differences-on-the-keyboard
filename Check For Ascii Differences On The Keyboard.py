print(50*"=")
print("Check For Ascii Differences On The Keyboard")
print(50*"=")

total = int(input("jumlah kata yang ingin dicari: ")) #user menginputkan berapa kata yang ingin di masukan
lis_usr = [] #ini adalah list kosong yang digunakan untuk menampung data dari user

while total > 0 :#while ini di gunakan untuk perulangan
    inp_usr = input("Masukan Kata: ")
    lis_usr.append(inp_usr)#perintah append di gunakan untuk menambahkan data pada list dan juga menyimpan inputan dari user
    total -= 1

for x in lis_usr: #ini adalah perulangan 
    print ("hasil: ")
    for i in range(0, len(x)):
        if i == 0:
            continue#perintah continue digunakan untuk melompati pada 
        hrf_sebelum = x[i-1]
        hrf_sesudah = x[i]

        selisih = ord(hrf_sebelum) - ord(hrf_sesudah)#untuk menghitung selisih ascii menggunakan perintah (-) dan untuk perintah ord digunakan untuk melihat ascii
        if selisih < 0 : #jika selisih kurang dari 0 
            selisih = -(selisih)#untuk (-)selisih digunakan agar hasil tidak bernilai negatif
        
        elif ord(hrf_sebelum) < ord(hrf_sesudah):
            print(hrf_sebelum, "kurang dari", hrf_sesudah, "selisihnya adalah",selisih)
        else:
            print(hrf_sebelum, "lebih dari", hrf_sesudah, "selisihnya adalah",selisih)

