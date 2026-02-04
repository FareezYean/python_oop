# buat nama class
class cat :
    # __init__ = konstruktor = yang pertama kali dijalankan
    # definisikan atribut dalam konstruktor
    def __init__(self, color, height):
        self.color = color
        self.height = height

# buat objek dari class cat
garfield = cat("orange", 25)
touman = cat("white", 20)

# debug objek di memory (muncul adress memory)
print("obj garfield :", garfield)
print("obj touman   :", touman)

# panggil atribut objek
print(f"warna garfield :, {garfield.color}")
print(f"berat touman   :, {touman.height}")