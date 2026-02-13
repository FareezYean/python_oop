class Akun:
    def __init__(self, nama, nis, password):
        self.nama = nama
        self.nis = nis
        self.__password = password

    def cek_password(self, input_password):
        return self.__password == input_password
