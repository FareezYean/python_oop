data = []

def tambah_data():
    nama = input("Masukkan nama: ")
    umur = input("Masukkan umur: ")
    data.append({"nama": nama, "umur": umur})
    print("================")
    print("Data berhasil ditambahkan\n")

def tampil_data():
    if len(data) == 0:
        print("Data tidak ada\n")
    else:
        print("\n===== DATA =====")
        i = 0
        while i < len(data):
            print("Nama :", data[i]["nama"])
            print("Umur :", data[i]["umur"])
            i = i + 1

def ubah_data():
    tampil_data()
    if len(data) > 0:
        index = int(input("Pilih nomor data (ketik 1): ")) - 1
        print("================")

        if index >= 0 and index < len(data):
            print("1. Ubah nama")
            print("2. Ubah umur")
            print("3. Ubah semua")
            pilihan = input("Pilih: ")

            if pilihan == "1":
                data[index]["nama"] = input("Masukkan nama baru: ")
            elif pilihan == "2":
                data[index]["umur"] = input("Masukkan umur baru: ")
            elif pilihan == "3":
                data[index]["nama"] = input("Masukkan nama baru: ")
                data[index]["umur"] = input("Masukkan umur baru: ")
            else:
                print("Pilihan tidak ada")

            print("Data berhasil diubah\n")
        else:
            print("Nomor tidak valid\n")

def hapus_data():
    tampil_data()
    if len(data) > 0:
        index = int(input("Pilih nomor data (ketik 1): ")) - 1
        print("================")

        if index >= 0 and index < len(data):
            print("1. Hapus data ini")
            print("2. Batal")
            pilihan = input("Pilih: ")

            if pilihan == "1":
                data.pop(index)
                print("Data berhasil dihapus\n")
            else:
                print("Penghapusan dibatalkan\n")
        else:
            print("Nomor tidak valid\n")

while True:
    print("===== MENU =====")
    print("1. Tambah data")
    print("2. Tampilkan data")
    print("3. Ubah data")
    print("4. Hapus data")
    print("0. Keluar")
    print("================")

    menu = input("Pilih menu: ")

    if menu == "1":
        tambah_data()
    elif menu == "2":
        tampil_data()
    elif menu == "3":
        ubah_data()
    elif menu == "4":
        hapus_data()
    elif menu == "0":
        print("Program selesai")
        break
    else:
        print("Menu tidak tersedia\n")
