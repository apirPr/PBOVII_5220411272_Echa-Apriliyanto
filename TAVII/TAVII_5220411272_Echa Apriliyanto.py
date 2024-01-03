"""
SISTEM MANAJEMEN TARI
"""

import random


class Tari:
    def __init__(self, nama, skor_popularitas, asal, ciri_ciri):
        self.__nama = nama
        self.__skor_popularitas = skor_popularitas
        self._asal = asal
        self._ciri_ciri = ciri_ciri

    def get_nama(self):
        return self.__nama

    def get_skor_popularitas(self):
        return self.__skor_popularitas

    def tampilkan_info(self):
        print("===== Informasi Tari =====")
        print("Nama: ", self.__nama)
        print("Skor Popularitas: ", self.__skor_popularitas)
        print("Asal: ", self._asal)
        print("Ciri-ciri: ", self._ciri_ciri)

    def pentaskan(self):
        print(f"{self.get_nama()} sedang dipentaskan")
        self.__skor_popularitas += random.randint(1, 100)

    def _lestarikan(self):
        print(f"{self.get_nama()} sedang dilestarikan")
        keberhasilan = random.randint(1, 10)

        if keberhasilan > 5:
            self.__skor_popularitas += keberhasilan
            print(f"{self.get_nama()} berhasil dilestarikan!")
            return True
        else:
            print(f"Upaya pelestarian {self.get_nama()} gagal!")
            return False


class TariTradisional(Tari):
    def __init__(self, properti_tari, nama, skor_popularitas, asal, ciri_ciri):
        super().__init__(nama, skor_popularitas, asal, ciri_ciri)
        self._daftar_lomba = []
        self.properti_tari = properti_tari  # list

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Properti Tari: ", self.properti_tari)
        print("Daftar Lomba Yang Pernah Diadakan: ")
        for i in range(len(self._daftar_lomba)):
            print(f"    {i + 1}. ", self._daftar_lomba[i])

    def adakan_lomba(self, judul_lomba, tanggal, lokasi):
        lomba = {"judul_lomba": judul_lomba, "tanggal": tanggal, "lokasi": lokasi}
        self._daftar_lomba.append(lomba)
        print(f"{judul_lomba} berhasil diselenggarakan!")


class TariKontemporer(Tari):
    def __init__(self, tema, konsep_musik, nama, skor_popularitas, asal, ciri_ciri):
        super().__init__(nama, skor_popularitas, asal, ciri_ciri)
        self.tema = tema
        self.konsep_musik = konsep_musik
        self._daftar_workshop = []

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Tema: ", self.tema)
        print("Konsep Musik: ", self.konsep_musik)
        print("Daftar Workshop Yang Pernah Diadakan: ")
        for i in range(len(self._daftar_workshop)):
            print(f"    {i + 1}. ", self._daftar_workshop[i])

    def __adakan_workshop(self, judul_workshop, tanggal, lokasi):
        workshop = {
            "judul_workshop": judul_workshop,
            "tanggal": tanggal,
            "lokasi": lokasi,
        }
        self._daftar_workshop.append(workshop)
        print(f"{judul_workshop} berhasil diselenggarakan!")


class TariJawa(TariTradisional):
    def __init__(
        self, jawa_bagian, properti_tari, nama, skor_popularitas, asal, ciri_ciri
    ):
        super().__init__(properti_tari, nama, skor_popularitas, asal, ciri_ciri)
        self.jawa_bagian = jawa_bagian

    def tampilkan_info(self):
        super().tampilkan_info()
        print("Jawa Bagian: ", self.jawa_bagian)


tari_jaipong = TariTradisional(
    ["Kipas", "Selendang"],
    "Tari Jaipong",
    100,
    "Jawa Barat",
    "Gerakan yang dinamis namun lemah gemulai",
)
korean_dance = TariKontemporer(
    "Korea",
    "Musik K-Pop",
    "Korean Dance",
    100,
    "Korea",
    "Gerakan yang dinamis dan lincah",
)
tari_topeng = TariJawa(
    "Jawa Barat",
    ["Topeng", "Kipas"],
    "Tari Topeng",
    100,
    "Jawa Barat",
    "Gerakan yang gagah dan dinamis",
)

print("=" * 70)
for tari in [tari_jaipong, korean_dance, tari_topeng]:
    tari.pentaskan()
    print()
    tari._lestarikan()
    print()

    if isinstance(tari, TariTradisional):
        for _ in range(random.randint(3, 5)):
            lomba_ke_n = random.randint(1, 10)

            while lomba_ke_n in [lomba["judul_lomba"] for lomba in tari._daftar_lomba]:
                lomba_ke_n = random.randint(1, 10)

            tari.adakan_lomba(
                f"Lomba {tari.get_nama()}-{lomba_ke_n}",
                f"{random.randint(1,31)}-{random.randint(1,12)}-202{random.randint(1,5)}",
                "DKI Jakarta",
            )
        print()
    elif isinstance(tari, TariKontemporer):
        for _ in range(random.randint(3, 5)):
            workshop_ke_n = random.randint(1, 10)

            while workshop_ke_n in [
                workshop["judul_workshop"] for workshop in tari._daftar_workshop
            ]:
                workshop_ke_n = random.randint(1, 10)

            tari._TariKontemporer__adakan_workshop(
                f"Workshop {tari.get_nama()}-{workshop_ke_n}",
                f"{random.randint(1,31)}-{random.randint(1,12)}-202{random.randint(1,5)}",
                "DKI Jakarta",
            )
        print()

for tari in [tari_jaipong, korean_dance, tari_topeng]:
    tari.tampilkan_info()
    print("")
