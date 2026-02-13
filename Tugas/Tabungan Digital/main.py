from tabungan import Tabungan
from data_manager import load_data, save_data

def main():
    print("=== TABUNGAN DIGITAL SANTRI ===")

    data = load_data()

    nis = input("Masukkan NIS: ")

    # ================= LOGIN =================
    if nis in data:
        password = input("Masukkan Password: ")

        akun_data = data[nis]
        rekening = Tabungan(
            akun_data["nama"],
            nis,
            akun_data["password"],
            akun_data["saldo"]
        )

        if not rekening.cek_password(password):
            print("Password salah!")
            return

        print(f"\nSelamat datang kembali, {akun_data['nama']}!")

    # ================= REGISTRASI =================
    else:
        print("\nRekening belum ada, silakan daftar.")
        nama = input("Masukkan Nama: ")
        password = input("Buat Password: ")

        while True:
            try:
                saldo_awal = int(input("Saldo awal: "))
                if saldo_awal < 0:
                    print("Saldo tidak boleh negatif!")
                else:
                    break
            except ValueError:
                print("Input harus angka!")

        rekening = Tabungan(nama, nis, password, saldo_awal)

        data[nis] = {
            "nama": nama,
            "password": password,
            "saldo": saldo_awal
        }

        save_data(data)
        print("\nRekening berhasil dibuat!")

    # ================= MENU =================
    while True:
        print("\n==== MENU ====")
        print("1. Setor Tunai")
        print("2. Tarik Tunai")
        print("3. Cek Saldo")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            jumlah = int(input("Jumlah setor: "))
            rekening.setor(jumlah)

        elif pilihan == "2":
            jumlah = int(input("Jumlah tarik: "))
            rekening.tarik(jumlah)

        elif pilihan == "3":
            print(f"Saldo: Rp {rekening.get_saldo()}")

        elif pilihan == "0":
            data[nis]["saldo"] = rekening.get_saldo()
            save_data(data)
            print("Data disimpan. Terima kasih!")
            break

        else:
            print("Menu tidak valid!")

if __name__ == "__main__":
    main()
