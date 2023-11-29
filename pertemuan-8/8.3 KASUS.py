class PerpusItem:
    def __init__(self, judul, subjek, lokasi_penyimpanan):
        self.judul = judul
        self.subjek = subjek
        self.lokasi_penyimpanan = lokasi_penyimpanan
        self.kategori = (
            isinstance(self, Buku)
            and "Buku"
            or isinstance(self, Majalah)
            and "Majalah"
            or isinstance(self, DVD)
            and "DVD"
            or "Tidak diketahui"
        )

    def lokasi_menyimpan(self):
        print("Lokasi Penyimpanan: ", self.lokasi_penyimpanan)

    def info(self):
        if self.kategori == "Buku":
            print("Judul Buku: ", self.judul)
            print("ISBN: ", self.ISBN)
            print("Pengarang: ", {pengarang.nama for pengarang in self.pengarang})
            print("Jumlah Halaman: ", self.jmlHal)
            print("Ukuran: ", self.ukuran)
            self.lokasi_menyimpan()
        elif self.kategori == "Majalah":
            print("Judul Majalah: ", self.judul)
            print("Volume: ", self.volume)
            print("Issue: ", self.issue)
            self.lokasi_menyimpan()
        elif self.kategori == "DVD":
            print("Judul DVD: ", self.judul)
            print("Aktor: ", self.aktor)
            print("Genre: ", self.genre)
            self.lokasi_menyimpan()


class Katalog:
    def __init__(self, items=[]):
        self.items = items

    def cari(self, judul):
        for item in self.items:
            if item.judul == judul:
                print(f"{item.judul} tersedia")
                return item
        print(f"{judul} tidak tersedia")

    def tambah_item(self, item):
        self.items.append(item)

    def hapus_item(self, item):
        self.items.remove(item)


class Buku(PerpusItem):
    def __init__(
        self, judul, subjek, lokasi_penyimpanan, ISBN, pengarang, jmlHal, ukuran
    ):
        super().__init__(judul, subjek, lokasi_penyimpanan)
        self.ISBN = ISBN
        self.pengarang = pengarang
        self.jmlHal = jmlHal
        self.ukuran = ukuran


class Majalah(PerpusItem):
    def __init__(self, judul, subjek, lokasi_penyimpanan, volume, issue):
        super().__init__(judul, subjek, lokasi_penyimpanan)
        self.volume = volume
        self.issue = issue


class DVD(PerpusItem):
    def __init__(self, judul, subjek, lokasi_penyimpanan, aktor, genre):
        super().__init__(judul, subjek, lokasi_penyimpanan)
        self.aktor = aktor
        self.genre = genre


class Pengarang:
    def __init__(self, nama, buku=[]):
        self.nama = nama
        self.buku = buku

    def info(self):
        print("Nama Pengarang: ", self.nama)
        print("Buku yang ditulis: ", {buku.judul for buku in self.buku})

    def tambah_buku(self, buku):
        self.buku.append(buku)

    def cari(self, judul):
        for item in self.buku:
            if item.judul == judul:
                print(f"{item.judul} tersedia")
                return item
        print(f"{judul} tidak tersedia")

katalog_1 = Katalog()
katalog_2 = Katalog()
katalog_3 = Katalog()

pengarang_1 = Pengarang("Andi")
pengarang_2 = Pengarang("Budi")
pengarang_3 = Pengarang("Caca")
pengarang_4 = Pengarang("Dedi")
pengarang_5 = Pengarang("Eka")

buku_1 = Buku(
    "Pemrograman Python",
    "Pemrograman",
    "Lemari 10, Baris 1",
    "123-456-100",
    [pengarang_1, pengarang_2],
    100,
    "A4",
)
buku_2 = Buku(
    "Pemrograman Java",
    "Pemrograman",
    "Lemari 10, Baris 1",
    "123-456-101",
    [pengarang_1, pengarang_3],
    200,
    "A3",
)
buku_3 = Buku(
    "Pemrograman Go",
    "Pemrograman",
    "Lemari 10, Baris 1",
    "123-456-102",
    [pengarang_4, pengarang_5],
    300,
    "A4",
)

majalah_1 = Majalah("Tokyo Terror", "Crime", "Lemari 3, Baris 3", 1, 1)
majalah_2 = Majalah("Jakarta Night", "Social", "Lemari 3, Baris 2", 1, 2)
majalah_3 = Majalah("Bandung Fashion", "Trend", "Lemari 3, Baris 2", 2, 3)

dvd_1 = DVD(
    "Kuntilanak 9",
    "Horror Movies",
    "Lemari 4, Baris 1",
    ["Kevin", "D", "Mike", "Zahra"],
    "Horror",
)
dvd_2 = DVD(
    "Chainsaw 12",
    "Thriller Movies",
    "Lemari 4, Baris 2",
    ["Luvis", "Pakuan", "Mole", "Chandra"],
    "Thriller",
)
dvd_3 = DVD(
    "Pengabdi Setan",
    "Horror Movies",
    "Lemari 4, Baris 1",
    ["Rizky", "Rizal", "Rizwan", "Rizma"],
    "Horror",
)

katalog_1.tambah_item(buku_1)
katalog_1.tambah_item(dvd_1)
katalog_1.tambah_item(majalah_1)
katalog_2.tambah_item(buku_2)
katalog_2.tambah_item(majalah_2)
katalog_2.tambah_item(dvd_2)
katalog_3.tambah_item(majalah_3)
katalog_3.tambah_item(buku_3)
katalog_3.tambah_item(dvd_3)

pengarang_1.tambah_buku(buku_1)
pengarang_1.tambah_buku(buku_2)
pengarang_2.tambah_buku(buku_1)
pengarang_3.tambah_buku(buku_2)
pengarang_4.tambah_buku(buku_3)
pengarang_5.tambah_buku(buku_3)

katalog_1.cari("Pemrograman Python")
katalog_2.cari("Bandung Fashion")
katalog_3.cari("Pengabdi Setan")

print()
pengarang_1.info()
print()
pengarang_1.cari("Pemrograman Python")
pengarang_1.cari("10 Dosa Besar Hiruzen")
print()
buku_1.info()
print()
majalah_1.info()
print()
dvd_1.info()