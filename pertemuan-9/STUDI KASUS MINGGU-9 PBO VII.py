class Animal:
    def __init__(self, nama, sifat, ukuran, jumlah_kaki):
        self.__nama = nama
        self._sifat = sifat
        self.ukuran = ukuran
        self.jumlah_kaki = jumlah_kaki

    def get_nama(self):
        return self.__nama

    def set_nama(self, nama):
        self.__nama = nama

    # print informasi hewan
    def tampilkan_informasi_hewan(self):
        print("Nama: ", self.__nama)
        print("Sifat: ", self._sifat)
        print("Ukuran: ", self.ukuran)
        print("Jumlah Kaki: ", self.jumlah_kaki)


class Mamalia(Animal):
    def __init__(self, jenis_mamalia, bisa_jalan, nama, sifat, ukuran, jumlah_kaki):
        super().__init__(nama, sifat, ukuran, jumlah_kaki)
        self._jenis_mamalia = jenis_mamalia
        self.bisa_jalan = bisa_jalan

    def jalan(self):
        if self.bisa_jalan == True:
            print("tap tap tap")
        else:
            print(f"{self._jenis_mamalia} tidak bisa berjalan")

    def tampilkan_informasi_hewan(self):
        print("Nama: ", self.get_nama())
        print("Sifat: ", self._sifat)
        print("Ukuran: ", self.ukuran)
        print("Jumlah Kaki: ", self.jumlah_kaki)
        print("Jenis Mamalia: ", self._jenis_mamalia)
        print("Bisa Berjalan: ", self.bisa_jalan)


class Aves(Animal):
    def __init__(self, jenis_aves, bisa_terbang, nama, sifat, ukuran, jumlah_kaki):
        super().__init__(nama, sifat, ukuran, jumlah_kaki)
        self._jenis_aves = jenis_aves
        self.bisa_terbang = bisa_terbang

    def terbang(self):
        if self.bisa_terbang == True:
            print("wush")
        else:
            print(f"{self._jenis_aves} tidak bisa terbang")

    def tampilkan_informasi_hewan(self):
        print("Nama: ", self.get_nama())
        print("Sifat: ", self._sifat)
        print("Ukuran: ", self.ukuran)
        print("Jumlah Kaki: ", self.jumlah_kaki)
        print("Jenis Aves: ", self._jenis_aves)
        print("Bisa Terbang: ", self.bisa_terbang)

        if isinstance(self, Ayam):
            print("Bisa Diadu: ", self.bisa_diadu)


class Ayam(Aves):
    def __init__(self,jenis_ayam,bisa_diadu,jenis_aves,bisa_terbang,nama,sifat,ukuran,jumlah_kaki):
        super().__init__(jenis_aves, bisa_terbang, nama, sifat, ukuran, jumlah_kaki)
        self._jenis_ayam = jenis_ayam
        self.bisa_diadu = bisa_diadu

    def terbang(self):
        if self.bisa_terbang == True:
            print("ayam terbang menurun~")
        else:
            print(f"{self._jenis_ayam} tidak bisa terbang")

    def adu_ayam(self):
        if self.bisa_diadu == True:
            print("ayam beradu")
        else:
            print(f"{self._jenis_ayam} tidak bisa diadu")


class Merpati(Aves):
    def __init__(
        self, jenis_merpati, jenis_aves, bisa_terbang, nama, sifat, ukuran, jumlah_kaki
    ):
        super().__init__(jenis_aves, bisa_terbang, nama, sifat, ukuran, jumlah_kaki)
        self._jenis_merpati = jenis_merpati

    def terbang(self):
        print("merpati terbang dengan indah~")


# Mamalia yang tidak bisa berjalan
paus_biru = Mamalia("paus", False, "paus biru", "Karnivora", "besar", 0)
# Mamalia yang bisa berjalan
kucing = Mamalia("kucing", True, "kucing", "Karnivora", "kecil", 4)

# Aves yang tidak bisa terbang
burung_unta = Aves("burung unta", False, "burung unta", "Herbivora", "besar", 2)
# Aves yang bisa terbang
elang_jawa = Aves("elang jawa", True, "elang jawa", "Karnivora", "sedang", 2)

# Ayam yang tidak bisa diadu
ayam_hias = Ayam('ayam hias', False, 'ayam', False, 'ayam hias', 'Omnivora', 'kecil', 2)
# Ayam yang bisa diadu
ayam_bangkok = Ayam('ayam bangkok', True, 'ayam', False, 'ayam bangkok', 'Omnivora', 'kecil', 2)

# Ayam yang bisa terbang
ayam_hutan = Ayam('ayam hutan', True, 'ayam', True, 'ayam hutan', 'Omnivora', 'kecil', 2)

# Merpati
merpati_kipas = Merpati('merpati kipas', 'merpati', True, 'merpati kipas', 'Omnivora', 'kecil', 2)

paus_biru.tampilkan_informasi_hewan()
print()
kucing.tampilkan_informasi_hewan()
print()
burung_unta.tampilkan_informasi_hewan()
print()
elang_jawa.tampilkan_informasi_hewan()
print()
ayam_hias.tampilkan_informasi_hewan()
print()
ayam_bangkok.tampilkan_informasi_hewan()
print()
ayam_hutan.tampilkan_informasi_hewan()
print()
merpati_kipas.tampilkan_informasi_hewan()
print()

paus_biru.jalan()
print()
kucing.jalan()
print()

burung_unta.terbang()
print()
elang_jawa.terbang()
print()
ayam_hias.terbang()
print()

ayam_hias.adu_ayam()
print()
ayam_bangkok.adu_ayam()
print()
ayam_hutan.adu_ayam()
print()

merpati_kipas.terbang()
print()