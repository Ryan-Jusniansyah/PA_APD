import pwinput, time, os

def delay(seconds):
    time.sleep(seconds)
def clear():
    os.system("cls")

# Menyimpan Data
Pilihan_Topup = {
    "Mobile Legends" : {
        "15" : "8000",
        "35" : "14000",
        "50" : "26000",
    },
    "PUBG Mobile" : {
        "15" : "9000",
        "45" : "15000",
        "80" : "25000",
    },
    "Valorant" : {
        "50" : "15000",
        "100" : "25000",
        "200" : "45000",
    },
    "Free Fire" : {
        "5" : "5000",
        "25" : "12000",
        "50" : "20000",
    },
    "Point Blank" : {
        "1200" : "12000",
        "2400" : "24000",

    }
}

Metode_Pembayaran = {
    "Debit" : ["BCA", "Mandiri", "BRI"],
    "e-Money" : ["OVO", "DANA", "Shoppe Pay"]
}

Daftar_admin = {
    "Idad" : "Admin",
    "PasId" : "admin"
}

Daftar_akun = {
    "listakun" : [[], []]
}
indexakun = 0

Pembayaran_Debit = []
indexDebit = 0
Pembayaran_eMoney = []
indexeMoney = 0

def daftargame():
    print ("="*50)
    print ("Daftar Game".center(50))
    print ("="*50)
    print()
    index = 1
    for i in Pilihan_Topup.keys():
        print(f"[{index}] {i}")
        index += 1
    print()
    print("="*50)

def Admin():
    clear()
    delay(1)
    print("Anda Memilih Admin")
    delay(1)
    clear()
    print("="*50)
    print("ADMIN".center(50))
    print("="*50)
    print()
    username = input("masukkan ID Admin : ")
    password = pwinput.pwinput("masukkan password : ")
    print()
    print("="*50)
    if username == Daftar_admin["Idad"] and password == Daftar_admin["PasId"]:
        delay(0.5)
        clear()
        print ("anda berhasil login")
        delay(1.5)
        clear()
        Menu_admin()
    else:
        print("Id atau Password Salah!")
        delay(1)
        Admin()


def Menu_User():
    clear()
    delay(1)
    print("""
    ====================================
    |            MENU USER             |
    ====================================
    | [1] LOGIN                        |
    | [2] REGISTER                     |
    | [3] LOGOUT                       |
    ====================================
    """)
    pilih = input("Masukkan Pilihan Anda: ")
    if pilih == "1":
        Login_user()
    elif pilih == "2":
        Register_user()
    elif pilih == "3":
        LoginUtama()
    else:
        Menu_User()

def grubML():
    print("="*50)
    print("Mobile Legends".center(50))
    print("="*50)
    print()
    index = 1
    for i, j in Pilihan_Topup["Mobile Legends"].items():
        print(f"[{index}] {i} Diamonds: Rp. {j}")
        index += 1
    print()
    print("="*50)

def grubPUBG():
    print("="*50)
    print("PUBG Mobile".center(50))
    print("="*50)
    print()
    index = 1
    for i, j in Pilihan_Topup["PUBG Mobile"].items():
        print(f"[{index}] {i} UC: Rp. {j}")
        index += 1
    print()
    print("="*50)

def grubValorant():
    print("="*50)
    print("Valorant".center(50))
    print("="*50)
    print()
    index = 1
    for i, j in Pilihan_Topup["Valorant"].items():
        print(f"[{index}] {i} V: Rp. {j}")
        index += 1
    print()
    print("="*50)

def grubFreeFire():
    print("="*50)
    print("Free Fire".center(50))
    print("="*50)
    print()
    index = 1
    for i, j in Pilihan_Topup["Free Fire"].items():
        print(f"[{index}] {i} Diamonds: Rp. {j}")
        index += 1
    print()
    print("="*50)

def grubPB():
    print("="*50)
    print("Point Blank".center(50))
    print("="*50)
    print()
    index = 1
    for i, j in Pilihan_Topup["Point Blank"].items():
        print(f"[{index}] {i} Cash: Rp. {j}")
        index += 1
    print()
    print("="*50)

def tam_ML():
    while True :
        clear()
        delay(1)
        grubML()
        pil = input("Mau Nambah Pilihan dan Harga? [Y/N] : ")
        if pil == "Y" or pil == "y":
            tam_pil = input("Masukkan Pilihan Baru Anda: ")
            tam_Harga = input("Masukkan Harga Terbaru: ")
            Pilihan_Topup["Mobile Legends"].update({tam_pil : tam_Harga})
            print("="*50)
            clear()
            delay(0.5)
            print("Pembaruan Anda Sudah Berhasil!!!")
            delay(1.5)
            clear()
        elif pil == "N" or pil == "n":
            clear()
            delay(0.5)
            print("="*50)
            print("Anda Tidak Ingin Menambah Lagi!".center(50))
            print("="*50)
            delay(1.5)
            clear()
            break
        else :
            print("error")

def tam_PUBG():
    while True :
        clear()
        delay(1)
        grubPUBG()
        pil = input("Mau Nambah Pilihan dan Harga? [Y/N] : ")
        if pil == "Y" or pil == "y":
            tam_pil = input("Masukkan Pilihan Baru Anda: ")
            tam_Harga = input("Masukkan Harga Terbaru: ")
            Pilihan_Topup["PUBG Mobile"].update({tam_pil : tam_Harga})
            print("="*50)
            clear()
            delay(0.5)
            print("Pembaruan Anda Sudah Berhasil!!!")
            delay(1.5)
            clear()
        elif pil == "N" or pil == "n":
            clear()
            delay(0.5)
            print("="*50)
            print("Anda Tidak Ingin Menambah Lagi!".center(50))
            print("="*50)
            delay(1.5)
            clear()
            break
        else :
            print("error")


def tam_Valorant():
    while True :
        clear()
        delay(1)
        grubValorant()
        pil = input("Mau Nambah Pilihan dan Harga? [Y/N] : ")
        if pil == "Y" or pil == "y":
            tam_pil = input("Masukkan Pilihan Baru Anda: ")
            tam_Harga = input("Masukkan Harga Terbaru: ")
            Pilihan_Topup["Valorant"].update({tam_pil : tam_Harga})
            print("="*50)
            clear()
            delay(0.5)
            print("Pembaruan Anda Sudah Berhasil!!!")
            delay(1.5)
            clear()
        elif pil == "N" or pil == "n":
            clear()
            delay(0.5)
            print("="*50)
            print("Anda Tidak Ingin Menambah Lagi!")
            print("="*50)
            delay(1.5)
            clear()
            break
        else :
            print("error")

def tam_Freefire():
    while True :
        clear()
        delay(1)
        grubFreeFire()
        pil = input("Mau Nambah Pilihan dan Harga? [Y/N] : ")
        if pil == "Y" or pil == "y":
            tam_pil = input("Masukkan Pilihan Baru Anda: ")
            tam_Harga = input("Masukkan Harga Terbaru: ")
            Pilihan_Topup["Free Fire"].update({tam_pil : tam_Harga})
            print("="*50)
            clear()
            delay(0.5)
            print("Pembaruan Anda Sudah Berhasil!!!")
            delay(1.5)
            clear()
        elif pil == "N" or pil == "n":
            clear()
            delay(0.5)
            print("="*50)
            print("Anda Tidak Ingin Menambah Lagi!")
            print("="*50)
            delay(1.5)
            clear()
            break
        else :
            print("error")

def tam_PB():
    while True :
        clear()
        delay(1)
        grubPB()
        pil = input("Mau Nambah Pilihan dan Harga? [Y/N] : ")
        if pil == "Y" or pil == "y":
            tam_pil = input("Masukkan Pilihan Baru Anda: ")
            tam_Harga = input("Masukkan Harga Terbaru: ")
            Pilihan_Topup["Point Blank"].update({tam_pil : tam_Harga})
            print("="*50)
            clear()
            delay(0.5)
            print("Pembaruan Anda Sudah Berhasil!!!")
            delay(1.5)
            clear()
        elif pil == "N" or pil == "n":
            clear()
            delay(0.5)
            print("="*50)
            print("Anda Tidak Ingin Menambah Lagi!")
            print("="*50)
            delay(1.5)
            clear()
            break
        else :
            print("error")

def Tambah_Harga():
    try:
        delay(0.5)
        clear()
        daftargame()
        print ("="*50)
        print ("Pilihan".center(50))
        print ("="*50)
        pil = int(input("Masukkan Pilihan Anda: "))
        if pil == 1:
            tam_ML()
        elif pil == 2:
            tam_PUBG()
        elif pil == 3:
            tam_Valorant()
        elif pil == 4:
            tam_Freefire()
        elif pil == 5:
            tam_PB()
        else:
            print("Pilihan Anda Tidak Ada Di Menu")
            delay(1)
            clear()
            Tambah_Harga()
    except ValueError:
        delay(1)
        clear()
        print("Masukkan angka!!")
        delay(1)
        clear()
        Tambah_Harga()

def del_ML():
    while True :
        clear()
        delay(1)
        grubML()
        pil = input("Mau Hapus Pilihan dan Harga? [Y/N] : ")
        if pil == "Y" or pil == "y":
            hap_pil = input("Masukkan pilihan yang mau dihapus: ")
            del Pilihan_Topup["Mobile Legends"][hap_pil]
            clear()
            delay(0.5)
            print("Pilihan telah terhapus!!")
            delay(1.5)
            clear()
        elif pil == "N" or pil == "n":
            clear()
            delay(0.5)
            print("="*50)
            print("Anda Tidak Ingin Menghapus Lagi!".center(50))
            print("="*50)
            delay(1.5)
            clear()
            break
        else :
            print("Inputan anda salah")

def del_PUBG():
    while True :
        clear()
        delay(1)
        grubPUBG()
        print("="*50)
        pil = input("Mau Hapus Pilihan dan Harga? [Y/N] : ")
        if pil == "Y" or pil == "y":
            hap_pil = input("Masukkan pilihan yang mau dihapus: ")
            del Pilihan_Topup["PUBG Mobile"][hap_pil]
            clear()
            delay(0.5)
            print("Pilihan telah terhapus!!")
            delay(1.5)
            clear()
        elif pil == "N" or pil == "n":
            clear()
            delay(0.5)
            print("="*50)
            print("Anda Tidak Ingin Menghapus Lagi!".center(50))
            print("="*50)
            delay(1.5)
            clear()
            break
        else :
            print("Inputan anda salah")

def del_Valorant():
    while True :
        clear()
        delay(1)
        grubValorant()
        pil = input("Mau Hapus Pilihan dan Harga? [Y/N] : ")
        if pil == "Y" or pil == "y":
            hap_pil = input("Masukkan pilihan yang mau dihapus: ")
            del Pilihan_Topup["Valorant"][hap_pil]
            clear()
            delay(0.5)
            print("Pilihan telah terhapus!!")
            delay(1.5)
            clear()
        elif pil == "N" or pil == "n":
            clear()
            delay(0.5)
            print("="*50)
            print("Anda Tidak Ingin Menghapus Lagi!".center(50))
            print("="*50)
            delay(1)
            clear()
            break
        else :
            print("Inputan anda salah")

def del_Freefire():
    while True :
        clear()
        delay(1)
        grubFreeFire()
        pil = input("Mau Hapus Pilihan dan Harga? [Y/N] : ")
        if pil == "Y" or pil == "y":
            hap_pil = input("Masukkan pilihan yang mau dihapus: ")
            del Pilihan_Topup["Free Fire"][hap_pil]
            clear()
            delay(0.5)
            print("Pilihan telah terhapus!!")
            delay(1.5)
            clear()
        elif pil == "N" or pil == "n":
            clear()
            delay(0.5)
            print("="*50)
            print("Anda Tidak Ingin Menghapus Lagi!".center(50))
            print("="*50)
            delay(1.5)
            clear()
            break
        else :
            print("Inputan anda salah")

def del_PB():
    while True :
        clear()
        delay(1)
        grubPB()
        print("="*50)
        pil = input("Mau Hapus Pilihan dan Harga? [Y/N] : ")
        if pil == "Y" or pil == "y":
            hap_pil = input("Masukkan pilihan yang mau dihapus: ")
            del Pilihan_Topup["Point Blank"][hap_pil]
            clear()
            delay(0.5)
            print("Pilihan telah terhapus!!")
            delay(1.5)
            clear()
        elif pil == "N" or pil == "n":
            clear()
            delay(0.5)
            print("="*50)
            print("Anda Tidak Ingin Menghapus Lagi!".center(50))
            print("="*50)
            delay(1.5)
            clear()
            break
        else :
            print("Inputan anda salah")

def Hapus_harga():
    try:
        delay(1)
        clear()
        print ("="*50)
        print ("Anda Ingin Mengapus Pilihan Dan Harga".center(50))
        print ("="*50)
        delay(1)
        clear()
        daftargame()
        pilih = int(input("Masukkan Pilihan Anda: "))
        if pilih == 1:
            del_ML()
        elif pilih == 2:
            del_PUBG()
        elif pilih == 3:
            del_Valorant()
        elif pilih == 4:
            del_Freefire()
        elif pilih == 5:
            del_PB()
        else:
            print("Pilihan Anda Tidak Ada Di Menu")
            delay(1)
            Hapus_harga()
    except ValueError:
        delay(1)
        clear()
        print("Masukkan angka!!")
        delay(1)
        clear()
        Hapus_harga()

def ubah_ML():
    while True :
        clear()
        delay(1)
        grubML()
        pil = input("Mau Ubah Pilihan dan Harga ? [Y/N] : ")
        if pil == "Y" or pil == "y":
            ubah_pil = input("Masukkan Pilihan Yang Anda Mau Rubah? : ")
            hargaBaru = input("masukkan harga baru: ")
            Pilihan_Topup["Mobile Legends"].update({ubah_pil: hargaBaru})

            print (f"{ubah_pil} Diamonds telah diganti menjadi {ubah_pil} Diamonds: Rp. {hargaBaru}\n")
            delay(1)
            clear()
        elif pil == "N" or pil == "n":
            clear()
            delay(0.5)
            print("Anda Tidak Ingin Merubah Lagi!")
            delay(1.5)
            clear()
            break
        else :
            print("error")

def ubah_PUBG():
    while True :
        clear()
        delay(1)
        grubPUBG()
        pil = input("Mau Ubah Pilihan dan Harga ? [Y/N] : ")
        if pil == "Y" or pil == "y":
            ubah_pil = input("Masukkan Pilihan Yang Anda Mau Rubah? : ")
            hargaBaru = input("masukkan harga baru: ")
            Pilihan_Topup["PUBG Mobile"].update({ubah_pil: hargaBaru})

            print (f"{ubah_pil} UC telah diganti menjadi {ubah_pil} UC: Rp. {hargaBaru}\n")
            delay(1)
            clear()
        elif pil == "N" or pil == "n":
            clear()
            delay(0.5)
            print("Anda Tidak Ingin Merubah Lagi!")
            delay(1.5)
            clear()
            break
        else :
            print("error")

def ubah_Valorant():
    while True :
        clear()
        delay(1)
        grubValorant()
        pil = input("Mau Ubah Pilihan dan Harga ? [Y/N] : ")
        if pil == "Y" or pil == "y":
            ubah_pil = input("Masukkan Pilihan Yang Anda Mau Rubah? : ")
            hargaBaru = input("masukkan harga baru: ")
            Pilihan_Topup["Valorant"].update({ubah_pil: hargaBaru})

            print (f"{ubah_pil} V telah diganti menjadi {ubah_pil} V: Rp. {hargaBaru}\n")
            delay(1)
            clear()
        elif pil == "N" or pil == "n":
            clear()
            delay(0.5)
            print("Anda Tidak Ingin Merubah Lagi!")
            delay(1.5)
            clear()
            break
        else :
            print("error")

def ubah_Freefire():
    while True :
        clear()
        delay(1)
        grubFreeFire()
        pil = input("Mau Ubah Pilihan dan Harga ? [Y/N] : ")
        if pil == "Y" or pil == "y":
            ubah_pil = input("Masukkan Pilihan Yang Anda Mau Rubah? : ")
            hargaBaru = input("masukkan harga baru: ")
            Pilihan_Topup["Free Fire"].update({ubah_pil: hargaBaru})

            print (f"{ubah_pil} Diamonds telah diganti menjadi {ubah_pil} Diamonds: Rp. {hargaBaru}\n")
            delay(1)
            clear()
        elif pil == "N" or pil == "n":
            clear()
            delay(0.5)
            print("Anda Tidak Ingin Merubah Lagi!")
            delay(1.5)
            clear()
            break
        else :
            print("error")

def ubah_PB():
    while True :
        clear()
        delay(1)
        grubPB()
        pil = input("Mau Ubah Pilihan dan Harga ? [Y/N] : ")
        if pil == "Y" or pil == "y":
            ubah_pil = input("Masukkan Pilihan Yang Anda Mau Rubah? : ")
            hargaBaru = input("masukkan harga baru: ")
            Pilihan_Topup["Point Blank"].update({ubah_pil: hargaBaru})

            print (f"{ubah_pil} Cash telah diganti menjadi {ubah_pil} Cash: Rp. {hargaBaru}\n")
            delay(1)
            clear()
        elif pil == "N" or pil == "n":
            clear()
            delay(0.5)
            print("Anda Tidak Ingin Merubah Lagi!")
            delay(1.5)
            clear()
            break
        else :
            print("error")

def Ubah_harga():
    try:
        delay(0.5)
        clear()
        print ("="*50)
        print ("Anda Ingin Merubah Pilihan & Harga".center(50))
        print ("="*50)
        delay(1)
        clear()
        daftargame()
        pilih = int(input("Masukkan Pilihan Anda: "))
        if pilih == 1:
            ubah_ML()
        elif pilih == 2:
            ubah_PUBG()
        elif pilih == 3:
            ubah_Valorant()
        elif pilih == 4:
            ubah_Freefire()
        elif pilih == 5:
            ubah_PB()
        else:
            print("Pilihan Anda Tidak Ada Di Menu!")
            delay(1)
            Ubah_harga()
    except ValueError:
        delay(1)
        clear()
        print("Masukkan angka!!")
        delay(1)
        clear()
        Ubah_harga()

def ulang():
    while True :
        ulang = input("Apakah Anda Ingin Kembali Ke Menu [Y/N]: ")
        #if ulang == "Y" or ulang == "y":
        #    Lihat_harga()
        if ulang == "Y" or ulang == "y":
            clear()
            delay(1)
            print("Anda Akan Kembali Ke Menu!")
            delay(1)
            clear()
            break

def Lihat_harga():
    try:
        clear()
        delay(1)
        daftargame()
        pilih = int(input("Masukkan Pilihan Yang Mau Dicek Harganya?: "))
        if pilih == 1:
            clear()
            delay(1)
            grubML()
            ulang()
        elif pilih == 2:
            clear()
            delay(1)
            grubPUBG()
            ulang()
        elif pilih == 3:
            clear()
            delay(1)
            grubValorant()
            ulang()
        elif pilih == 4:
            clear()
            delay(1)
            grubFreeFire()
            ulang()
        elif pilih == 5:
            clear()
            delay(1)
            grubPB()
            ulang()
        else:
            print("Pilihan Anda Tidak Ada Di Menu!")
            delay(1)
            Lihat_harga()
    except ValueError:
        delay(1)
        clear()
        print("Masukkan Angka!!")
        delay(1)
        clear()
        Lihat_harga()

def Menu_admin():
    try:
        while True:
            print("""
            ====================================
            |            MENU ADMIN            |
            ====================================
            | [1] TAMBAH HARGA                 |
            | [2] HAPUS HARGA                  |
            | [3] UBAH HARGA                   |
            | [4] LIHAT HARGA                  |
            | [5] LOGOUT                       |
            ====================================
            """)
            Pilih = int(input("Masukkan Pilihan Anda: "))
            if Pilih == 1:
                Tambah_Harga()
            elif Pilih == 2:
                Hapus_harga()
            elif Pilih == 3:
                Ubah_harga()
            elif Pilih == 4:
                Lihat_harga()
            elif Pilih == 5:
                break
            else:
                print("Pilihan Anda Tidak Ada Di Menu")
                delay(1)
                Menu_admin()
    except ValueError:
        delay(1)
        clear()
        print("Masukkan Angka!!")
        delay(1)
        clear()
        Menu_admin()

def Login_user():
    indexakun = 0
    if len(Daftar_akun["listakun"][0]) == 0:
        print("Anda belum memiliki Akun! Silahkan Registrasi dulu.")
        userBaru = input("Masukkan Username baru: ")
        sandiBaru = input("Masukkan Password baru: ")
        print("Selamat Anda Telah Terdaftar")

        Daftar_akun["listakun"][0].append(userBaru)
        Daftar_akun["listakun"][1].append(sandiBaru)
        delay(0.5)
        clear()
        Menu_User()

    else:
        clear()
        delay(1)
        print("="*50)
        print("LOGIN".center(50))
        print("="*50)
        print()
        user = input("Masukkan Username: ")
        sandi = pwinput.pwinput("Masukkan Password: ")
        print()
        print("="*50)
        for iduser in range(len(Daftar_akun["listakun"][0])):
            if Daftar_akun["listakun"][0][iduser] == user:
                indexakun += iduser
            
        if Daftar_akun["listakun"][1][indexakun] == sandi:
            delay(1)
            print("Anda Telah Berhasil Login!")
            delay(1)
            clear()
            Menu_Topup()

def Register_user():
    clear()
    print("="*50)
    print("REGISTER".center(50))
    print("="*50)
    print()
    userBaru = input("Masukkan Username Baru: ")
    sandiBaru = input("Masukkan Password Baru: ")
    print()
    print("="*50)
    delay(1)
    print("Anda Telah Registrasi!!")

    Daftar_akun["listakun"][0].append(userBaru)
    Daftar_akun["listakun"][1].append(sandiBaru)
    clear()
    Menu_User()

def LoginUtama():
    try:
        while True :
            clear()
            print("""
            ============================================
            |       Selamat Datang Di TOP-UPkU         |
            ============================================
            | [1] ADMIN                                |
            | [2] USER                                 |
            | [3] EXIT                                 |
            ============================================
            """)
            pilih = int(input("Masukkan Pilihan Anda: "))
            if pilih == 1:
                Admin()
            elif pilih == 2:
                Menu_User()
            elif pilih == 3:
                clear()
                delay(1)
                print("""
                ============================
                |                          |
                |     'THANKS FOR USE'     |
                |       'MY PROGRAM'       |
                |                          |
                ============================ 
                """)
                delay(1)
                exit()
            else:
                LoginUtama()
    except ValueError:
        delay(1)
        clear()
        print("Masukkan Angka!!")
        delay(1)
        clear()
        LoginUtama()

def BayarDebit(pilih):
    clear()
    delay(1)
    print("="*50)
    if pilih == 1:
        print("BCA".center(50))
    elif pilih == 2:
        print("MANDIRI".center(50))
    elif pilih == 3:
        print("BRI".center(50))
    print("="*50)
    rek = int(input("Masukkan No. Rek: "))
    email = input("Masukkan Email: ")
    no_Hp = int(input("Masukkan No. Hp: "))
    Pembayaran_Debit.append(dict(Rekening=rek, account=email, nomor=no_Hp))
    print("="*50)
    print("Pembayaran Selesai!!")
    kembali = input("Kembali Ke Menu Awal? [Y/N]: ")
    if kembali == "Y" or kembali == "y":
        print("Terima Kasih Telah Membeli")
        delay(1)
        clear()
        Menu_Topup()
    elif kembali == "N" or kembali == "n":
        delay(1)
        clear()
        topUp()

def debit():
    try:    
        clear()
        delay(1)
        print("="*50)
        print("DEBIT".center(50))
        print("="*50)
        print()
        index = 1
        for i in Metode_Pembayaran["Debit"]:
            print(f"[{index}] {i}")
            index += 1
        index = 1
        print()
        print("="*50)
        Pilih = int(input("Masukkan Pilihan Anda: "))
        if Pilih == 1:
            BayarDebit(Pilih)
        elif Pilih == 2:
            BayarDebit(Pilih)
        elif Pilih == 3:
            BayarDebit(Pilih)
        else:
            print("Pilihan anda tidak ada di menu")
            debit()
    except ValueError:
        delay(1)
        clear()
        print("Masukkan Angka!!")
        delay(1)
        clear()
        debit()

def bayarE_Money(pilih):
    clear()
    delay(1)
    print("="*50)
    if pilih == 1:
        print("OVO".center(50))
    elif pilih == 2:
        print("DANA".center(50))
    elif pilih == 3:
        print("Shoppe Pay".center(50))
    print("="*50)
    email = input("Masukkan Email: ")
    no_Hp = int(input("Masukkan No. Hp: "))
    Pembayaran_eMoney.append(dict(account=email, nomor=no_Hp))
    print("="*50)
    print("Pembayaran Selesai!!")
    kembali = input("Kembali Ke Menu Awal? [Y/N]: ")
    if kembali == "Y" or kembali == "y":
        print("Terima Kasih Telah Membeli")
        delay(1)
        clear()
        Menu_Topup()
    elif kembali == "N" or kembali == "n":
        delay(1)
        clear()
        topUp()

def eMoney():
    try:
        print("="*50)
        print("e-Money".center(50))
        print("="*50)
        print()
        index = 1
        for i in Metode_Pembayaran["e-Money"]:
            print(f"[{index}] {i}")
            index += 1
        index = 1
        print()
        print("="*50)
        Pilih = int(input("Masukkan Pilihan Anda: "))
        if Pilih == 1:
            bayarE_Money(Pilih)
        elif Pilih == 2:
            bayarE_Money(Pilih)
        elif Pilih == 3:
            bayarE_Money(Pilih)
        else:
            eMoney()
    except ValueError:
        delay(1)
        clear()
        print("Masukkan Angka!!")
        delay(1)
        clear()
        eMoney()

def Method_Bayar():
    try:
        clear()
        delay(1)
        print("="*50)
        print("METODE PEMBAYARAN".center(50))
        print("="*50)
        print()
        index = 1
        for i in Metode_Pembayaran.keys():
            print(f"[{index}] {i}")
            index += 1
        index = 1
        print()
        print("="*50)
        pilih = int(input("Masukkan Pilihan Pembayaran: "))
        if pilih == 1:
            clear()
            delay(0.5)
            debit()
        elif pilih == 2:
            clear()
            delay(0.5)
            eMoney()
        else:
            print("Pilihan anda tidak ada di menu")
            Method_Bayar()
    except ValueError:
        delay(1)
        clear()
        print("Masukkan Angka!!")
        delay(1)
        clear()
        Method_Bayar()

def Topup_ML():
    clear()
    delay(1)
    grubML()
    angka = list(Pilihan_Topup["Mobile Legends"])
    pilih = int(input("Masukkan Pilihan Top-UP: "))
    pilih -= 1
    if pilih < 0 or pilih >= len(angka):
        print("Pilihan tidak ada!")
    else:
        Gem = angka[pilih]
        harga = Pilihan_Topup["Mobile Legends"][Gem]
        print(f"{Gem} Diamonds: Rp. {harga}")
        print(f"Yang Harus Anda Bayar ialah: Rp. {harga}")
        konfirm = input("Konfirmasi Lagi? (Y): ")
        if konfirm == "Y" or konfirm == "y":
            delay(1)
            clear()
            Method_Bayar()
        else:
            print("Pemilihan Gagal!")
            delay(1)
            clear()
            Menu_Topup()

def Topup_PUBGM():
    clear()
    delay(1)
    grubPUBG()
    angka = list(Pilihan_Topup["PUBG Mobile"])
    pilih = int(input("Masukkan Pilihan Top-UP: "))
    pilih -= 1
    if pilih < 0 or pilih >= len(angka):
        print("Pilihan tidak ada!")
    else:
        Gem = angka[pilih]
        harga = Pilihan_Topup["PUBG Mobile"][Gem]
        print(f"{Gem} UC: Rp. {harga}")
        print(f"Yang Harus Anda Bayar ialah: Rp. {harga}")
        konfirm = input("Konfirmasi Lagi? (Y): ")
        if konfirm == "Y" or konfirm == "y":
            delay(1)
            clear()
            Method_Bayar()
        else:
            print("Pemilihan Gagal!")
            delay(1)
            clear()
            Menu_Topup()       

def Topup_Valorant():
    clear()
    delay(1)
    grubValorant()
    angka = list(Pilihan_Topup["Valorant"])
    pilih = int(input("Masukkan Pilihan Top-UP: "))
    pilih -= 1
    if pilih < 0 or pilih >= len(angka):
        print("Pilihan tidak ada!")
    else:
        Gem = angka[pilih]
        harga = Pilihan_Topup["Valorant"][Gem]
        print(f"{Gem} V: Rp. {harga}")
        print(f"Yang Harus Anda Bayar ialah: Rp. {harga}")
        konfirm = input("Konfirmasi Lagi? (Y): ")
        if konfirm == "Y" or konfirm == "y":
            delay(1)
            clear()
            Method_Bayar()
        else:
            print("Pemilihan Gagal!")
            delay(1)
            clear()
            Menu_Topup()

def Topup_Freefire():
    clear()
    delay(1)
    grubFreeFire()
    angka = list(Pilihan_Topup["Free Fire"])
    pilih = int(input("Masukkan Pilihan Top-UP: "))
    pilih -= 1
    if pilih < 0 or pilih >= len(angka):
        print("Pilihan tidak ada!")
    else:
        Gem = angka[pilih]
        harga = Pilihan_Topup["Free Fire"][Gem]
        print(f"{Gem} Diamonds: Rp. {harga}")
        print(f"Yang Harus Anda Bayar ialah: Rp. {harga}")
        konfirm = input("Konfirmasi Lagi? (Y): ")
        if konfirm == "Y" or konfirm == "y":
            delay(1)
            clear()
            Method_Bayar()
        else:
            print("Pemilihan Gagal!")
            delay(1)
            clear()
            Menu_Topup()

def Topup_PB():
    clear()
    delay(1)
    grubPB()
    angka = list(Pilihan_Topup["Point Blank"])
    pilih = int(input("Masukkan Pilihan Top-UP: "))
    pilih -= 1
    if pilih < 0 or pilih >= len(angka):
        print("Pilihan tidak ada!")
    else:
        Gem = angka[pilih]
        harga = Pilihan_Topup["Point Blank"][Gem]
        print(f"{Gem} Cash: Rp. {harga}")
        print(f"Yang Harus Anda Bayar ialah: Rp. {harga}")
        konfirm = input("Konfirmasi Lagi? (Y): ")
        if konfirm == "Y" or konfirm == "y":
            delay(1)
            clear()
            Method_Bayar()
        else:
            print("Pemilihan Gagal!")
            delay(1)
            clear()
            Menu_Topup()            

def topUp():
    try:
        clear()
        delay(1)
        daftargame()
        pilih = int(input("Masukkan Pilihan Anda: "))
        if pilih == 1:
            Topup_ML()
        elif pilih == 2:
            Topup_PUBGM()
        elif pilih == 3:
            Topup_Valorant()
        elif pilih == 4:
            Topup_Freefire()
        elif pilih == 5:
            Topup_PB()
        else:
            print("Pilihan anda tidak ada di menu")
            topUp()
    except ValueError:
        delay(1)
        clear()
        print("Masukkan Angka!!!") 
        delay(1)
        clear()
        topUp()

def Menu_Topup():
    try:
        print("""
        ======================================
        |             TOP-UPkU               |
        ======================================
        | [1] TOP-UP                         |
        | [2] LOGOUT                         |
        ======================================
        """)
        pilih = int(input("Masukkan Pilihan Anda: "))
        if pilih == 1:
            clear()
            delay(1)
            topUp()
        elif pilih == 2:
            clear()
            delay(1)
            LoginUtama()
        else:
            print("Pilihan anda tidak ada di menu")
            Menu_Topup()
    except ValueError:
        delay(1)
        clear()
        print("Masukkan Angka!!!")
        delay(1)
        clear()
        Menu_Topup()

LoginUtama()