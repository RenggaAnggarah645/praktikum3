# Class Orang
class Orang:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia
    
    def greeting(self):
        print(f"Halo, nama saya {self.nama} dan saya berusia {self.usia} tahun.")

# Class Mahasiswa, mewarisi dari Orang
class Mahasiswa(Orang):
    def __init__(self, nama, usia, jurusan):
        super().__init__(nama, usia)
        self.jurusan = jurusan

    def greeting(self):
        print(f"Halo, nama saya {self.nama}, saya berusia {self.usia} tahun, dan saya kuliah di jurusan {self.jurusan}.")

# Contoh pemanggilan class dan metode
orang1 = Orang("Budi", 30)
orang1.greeting() # Output: "Halo, nama saya Budi dan saya berusia 30 tahun."

mahasiswa1 = Mahasiswa("Rina", 20, "Teknik Informatika")
mahasiswa1.greeting() # Output: "Halo, nama saya Rina, saya berusia 20 tahun, dan saya kuliah di jurusan Teknik Informatika."
