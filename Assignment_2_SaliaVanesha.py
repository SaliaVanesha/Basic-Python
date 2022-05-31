# Salia Vanesha_Basic Python_Assignment 2


"""
list_daftarKontak = []  
def tambahKontak(nama, noTelp):
    #with dictionary
    kontak = {
        #  "Key" : "Value"
        "Nama": nama,
        "NoTelp": noTelp
    }
    return kontak

list_daftarKontak.append(kontak)

belum menggunakan validasi, apakah no telp panjangnya sesuai
tidak bisa menginputkan +62xxxx sebagai no telp, terlalu banyak asumsi salah kemungkinan spasi dan huruf
"""

list_nama = []
list_noTelp =[]

def tambahKontak(nama, noTelp):
    list_nama.append(nama)
    list_noTelp.append(noTelp)
    print("Kontak telah berhasil ditambahkan")

def printDaftarKontak():
    print("Daftar Kontak")
    for i in range(len(list_nama)):
        print("Nama : {}".format(list_nama[i]))
        print("Nomor Telepon : 0{}".format(list_noTelp[i])) #masking 0 dengan asumsi menggunakan 0xxxxx

def daftarKontak():
    if len(list_nama) == 0 :
        print("Daftar Kontak Belum Tersedia, Silahkan pilih menu 2 untuk menambahkan kontak")
    else :
        printDaftarKontak()


print("Selamat datang!")
while True:
   print("""
   --Menu--
   1. Daftar Kontak
   2. Tambah Kontak
   3. Keluar
   """)

   user_input = int(input("Pilih Menu: "))

   if user_input == 1:
      daftarKontak()

   elif user_input == 2:
        input_nama = str(input("Nama: "))
        input_noTelp = int(input("Nomor Telepon: "))
        tambahKontak(input_nama, input_noTelp)

   elif user_input == 3:
      break
   
   else:
      print("Menu tidak tersedia dikarenakan anda salah memasukkan input (Pilih : 1/2/3)")

print("Program selesai, sampai jumpa!")