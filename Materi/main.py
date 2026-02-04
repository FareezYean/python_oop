print(" Hello World !!! ")
print(" Welcome To Class -Python Object Oriented Programming- ")
print(" Let's Learn Together ")

# cara membuat fungsi dengan def
# strukturnya : def - nama fungsi(parameter): 
def hello(name):
    print(f"Hello, {name}!")

hello("Alice")
hello("Bob")

# ==============================================================

def nilai(nama, uts, uas):
    rumus = (uts + uas) /2
    print(f"nilai {nama}: {rumus}")

nilai("Alice", 80, 90)
nilai("Bob", 90, 70)