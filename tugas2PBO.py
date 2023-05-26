class Mahasiswa: #Ini adalah definisi kelas untuk kelas Mahasiswa
    def __init__(self, nama, nim, jurusan):#Ini adalah metode untuk menginisialisasi atribut nama (nama), nim (NIM), dan jurusan (jurusan) dari objek mahasiswa
        self.nama = nama#untuk menyimpan nama mahasiswa dalam objek 
        self.nim = nim#untuk menyimpan nama mahasiswa dalam objek 
        self.jurusan = jurusan#untuk menyimpan jurusan mahasiswa dalam objek

    def tampilkan_info(self):#Ini adalah sebuah metode yang digunakan untuk menampilkan informasi mahasiswa seperti nama, NIM, dan jurusan
        print("Nama:", self.nama)#untuk mencetak nama mahasiswa
        print("NIM:", self.nim)#untuk mencetak NIM mahasiswa
        print("Jurusan:", self.jurusan.NamaJurusan)#untuk mencetak nama jurusan mahasiswa

class Jurusan:#Ini adalah definisi kelas untuk kelas Jurusan
    def __init__(self, nama_jurusan):#Ini adalah metode untuk menginisialisasikan atribut NamaJurusan (nama jurusan) dan sebuah daftar kosong DaftarMahasiswa (daftar mahasiswa) untuk objek jurusanya
        self.NamaJurusan = nama_jurusan#untuk menyimpan nama jurusan dalam objek Jurusan
        self.DaftarMahasiswa = []#untuk membuat daftar kosong yang akan digunakan untuk menyimpan daftar mahasiswa dalam objek Jurusan

    def tambah_mahasiswa(self, mahasiswa): #ini adalah untuk menambahkan objek Mahasiswa ke dalam daftar DaftarMahasiswa dari objek Jurusan
        self.DaftarMahasiswa.append(mahasiswa)#untuk menambahkan objek mahasiswa ke dalam daftar mahasiswa dalam objek Jurusan

    def tampilkan_daftar_mahasiswa(self):#untuk mencetak daftar mahasiswa pada objek jurusan
        print("Daftar Mahasiswa di Jurusan", self.NamaJurusan)#Ini adalah untuk melakukan iterasi melalui daftar DaftarMahasiswa dan mencetak nama dan NIM dari setiap mahasiswa
        for mahasiswa in self.DaftarMahasiswa:##untuk melakukan pengulangan (iterasi) melalui setiap objek mahasiswa dalam daftar mahasiswa dalam objek Jurusan
            print("Nama:", mahasiswa.nama)# untuk mencetak nama mahasiswa
            print("NIM:", mahasiswa.nim)#untuk mencetak NIM mahasiswa

class Universitas: #Ini adalah definisi kelas pada kelas Universitas
    def __init__(self, nama_universitas):#berfungsi untuk menginisialisasi atribut NamaUniversitas (nama universitas) dan sebuah daftar kosong DaftarJurusan (daftar jurusan) untuk objek universitas
        self.NamaUniversitas = nama_universitas#untuk menyimpan nama universitas dalam objek Universitas    
        self.DaftarJurusan = []#untuk membuat daftar kosong yang akan digunakan untuk menyimpan daftar jurusan dalam objek Universitas

    def tambah_jurusan(self, jurusan):#Ini adalah metode  untuk menambahkan sebuah jurusan ke dalam daftar DaftarJurusan di dalam objek Universitas
        self.DaftarJurusan.append(jurusan)#untuk menambahkan objek jurusan ke dalam daftar jurusan dalam objek Universitas

    def tampilkan_daftar_jurusan(self):#Ini adalah metode  untuk menampilkan daftar jurusan di dalam sebuah universitas.
        print("Daftar Jurusan di Universitas", self.NamaUniversitas)#untuk mencetak judul 
        for jurusan in self.DaftarJurusan:#untuk melakukan pengulangan (iterasi) melalui setiap objek jurusan dalam daftar jurusan dalam objek Universitas
            print("Nama Jurusan:", jurusan.NamaJurusan)#untuk mencetak nama jurusan

universitas_xyz = Universitas("XYZ University")#untuk Membuat objek Universitas dengan nama "XYZ University"

jurusan_ti = Jurusan("Teknik Informatika")# untuk Membuat objek Jurusan dengan nama "Teknik Informatika" dan menambahkannya ke dalam Universitas XYZ
universitas_xyz.tambah_jurusan(jurusan_ti)#untuk menambahkan objek jurusan

mahasiswa_rengga = Mahasiswa("Rengga Anggarah", "G1A022069", jurusan_ti) #untuk Membuat objek Mahasiswa dengan nama "Rengga Anggarah", NIM "G1A022069", dan memasukkannya ke dalam Jurusan Teknik Informatika di Universitas XYZ
jurusan_ti.tambah_mahasiswa(mahasiswa_rengga)#untuk menambahkan objek mahasiswa 

universitas_xyz.tampilkan_daftar_jurusan()# untuk Menampilkan daftar jurusan yang ada di Universitas XYZ
jurusan_ti.tampilkan_daftar_mahasiswa()#untuk Menampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ