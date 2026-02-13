from akun import Akun

class Tabungan(Akun):
    def __init__(self, nama, nis, password, saldo_awal): 
        super().__init__(nama, nis, password)
        self.__saldo = saldo_awal

    def get_saldo(self):
        return self.__saldo

    def setor(self, jumlah):
        if jumlah <= 0:
            print("Jumlah setor harus lebih dari 0!")
        else:
            self.__saldo += jumlah
            print("Saldo berhasil ditambahkan.")

    def tarik(self, jumlah):
        if jumlah <= 0:
            print("Jumlah tarik harus lebih dari 0!")
        elif jumlah > self.__saldo:
            print("Error: Saldo tidak cukup!")
        else:
            self.__saldo -= jumlah
            print("Penarikan berhasil.")
