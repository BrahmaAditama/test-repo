# fungsi tanpa parameter

# def NamaFungsi():
    # statement

def SuaraAyam():
    print("Kukuruyuk")

def HargaAyam():
    SuaraAyam()
    print("Harga ayam per kg adalah Rp. 20000")

HargaAyam()

# ======================================================
# fungsi dengan parameter

# def NamaFungsi(parameter):
    # statement

def HargaTotal(kg):
    total = kg*20000
    print("Harga", kg, " potong adalah Rp", total)

HargaTotal(2)

print(50*"=","\n")

def Guru(nama,pelajaran):
    print("nama guru =", nama)
    print("mengajar =", pelajaran, "\n")

Guru("Dea", "Seni")
Guru(nama="Endang", pelajaran="Olahraga")
Guru(pelajaran="Matematika", nama="Ujang")

# ======================================================
# fungsi dengan parameter default

# def NamaFungsi(parameter, parameter=default):
    # statement

def PenjagaSekolah(nama, sifat, shift="Siang"):
    print("nama pennjaga sekolah =", nama)
    print("shift =", shift)
    print("sifat =", sifat, "\n")

PenjagaSekolah("Saha", "Baik")
PenjagaSekolah(nama="Saha",shift="Malam", sifat="Galak")

# ======================================================
# fungsi dengan return

# def NamaFungsi(paramater):
    # retunr hasil

def Kuadrat(angka):
    return angka**2

print(Kuadrat(2))