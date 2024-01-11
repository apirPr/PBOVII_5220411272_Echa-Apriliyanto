import pymysql.cursors

# Untuk membuat tabel-tabel yang diperlukan jika belum ada:
with pymysql.connect(
    host="localhost",
    user="pbo",
    password="pbo",
    database="5220411272",
    cursorclass=pymysql.cursors.DictCursor,
) as connection:
    with connection.cursor() as cursor:
        sqls = [
            "CREATE TABLE perangkat_audio ( id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, merek VARCHAR(255) NOT NULL, harga INTEGER NOT NULL, jack_audio VARCHAR(255), wireless BOOLEAN );",
            "CREATE TABLE in_ear_monitor ( id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, merek VARCHAR(255) NOT NULL, harga INTEGER NOT NULL, jack_audio VARCHAR(255), wireless BOOLEAN, driver VARCHAR(255), detachable BOOLEAN );",
            "CREATE TABLE headphone ( id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, merek VARCHAR(255) NOT NULL, harga INTEGER NOT NULL, jack_audio VARCHAR(255), wireless BOOLEAN, jenis VARCHAR(255) );",
        ]
        for sql in sqls:
            cursor.execute(sql)
        connection.commit()


class PerangkatAudio:
    def __init__(self, merek, harga, jack_audio, wireless):
        self.__merek = merek
        self.__harga = harga
        self._jack_audio = jack_audio
        self.wireless = wireless

    def get_merek(self):
        return self.__merek

    def get_harga(self):
        return self.__harga

    def tampilkan_detail(self):
        print("Merek: ", self.get_merek())
        print("Harga: ", self.get_harga())
        print("Jack Audio: ", self._jack_audio)
        print("Wireless: ", self.wireless)

    def tambah_perangkat_ke_DB(self):
        with pymysql.connect(
            host="localhost",
            user="pbo",
            password="pbo",
            database="5220411272",
            cursorclass=pymysql.cursors.DictCursor,
        ) as connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO perangkat_audio (merek, harga, jack_audio, wireless) VALUES (%s, %s, %s, %s)"
                val = (
                    self.get_merek(),
                    self.get_harga(),
                    self._jack_audio,
                    self.wireless,
                )
                cursor.execute(sql, val)
                connection.commit()

    def tampilkan_tabel(self):
        with pymysql.connect(
            host="localhost",
            user="pbo",
            password="pbo",
            database="5220411272",
            cursorclass=pymysql.cursors.DictCursor,
        ) as connection:
            with connection.cursor() as cursor:
                sql = f"SELECT * FROM perangkat_audio;"
                cursor.execute(sql)
                rows = cursor.fetchall()

                output = ""
                for key, val in rows[0].items():
                    output += f"| {key}"
                print(output)
                print("-" * len(output))

                for row in rows:
                    output = ""
                    for key, val in row.items():
                        output += f"| {val}"
                    output = f"{output}"
                    print(output)

                connection.commit()

    def hapus_perangkat_dari_DB(self, id):
        with pymysql.connect(
            host="localhost",
            user="pbo",
            password="pbo",
            database="5220411272",
            cursorclass=pymysql.cursors.DictCursor,
        ) as connection:
            with connection.cursor() as cursor:
                sql = f"DELETE FROM perangkat_audio WHERE id = {id};"
                cursor.execute(sql)
                connection.commit()
    
    def perbarui_detail_perangkat_di_DB(self, id, data):
        with pymysql.connect(
            host="localhost",
            user="pbo",
            password="pbo",
            database="5220411272",
            cursorclass=pymysql.cursors.DictCursor,
        ) as connection:
            with connection.cursor() as cursor:
                for key, value in data.items():
                    sql = ""
                    if type(value) == "int":
                        sql = f"UPDATE headphone SET {key} = {value} WHERE id = {id};"
                    else:
                        sql = f"UPDATE headphone SET {key} = '{value}' WHERE id = {id};"
                    cursor.execute(sql)
                    connection.commit()



class InEarMonitor(PerangkatAudio):
    def __init__(self, merek, harga, jack_audio, wireless, driver, detachable):
        super().__init__(merek, harga, jack_audio, wireless)
        self.__driver = driver
        self.detachable = detachable

    def get_driver(self):
        return self.__driver

    def tampilkan_detail(self):
        super().tampilkan_detail()
        print("Driver: ", self.get_driver())
        print("Detachable: ", self.detachable)

    def tambah_perangkat_ke_DB(self):
        with pymysql.connect(
            host="localhost",
            user="pbo",
            password="pbo",
            database="5220411272",
            cursorclass=pymysql.cursors.DictCursor,
        ) as connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO in_ear_monitor (merek, harga, jack_audio, wireless, driver, detachable) VALUES (%s, %s, %s, %s, %s, %s)"
                val = (
                    self.get_merek(),
                    self.get_harga(),
                    self._jack_audio,
                    self.wireless,
                    self.get_driver(),
                    self.detachable,
                )
                cursor.execute(sql, val)
                connection.commit()

    def tampilkan_tabel(self):
        with pymysql.connect(
            host="localhost",
            user="pbo",
            password="pbo",
            database="5220411272",
            cursorclass=pymysql.cursors.DictCursor,
        ) as connection:
            with connection.cursor() as cursor:
                sql = f"SELECT * FROM in_ear_monitor;"
                cursor.execute(sql)
                rows = cursor.fetchall()

                output = ""
                for key, val in rows[0].items():
                    output += f"| {key}"
                print(output)
                print("-" * len(output))

                for row in rows:
                    output = ""
                    for key, val in row.items():
                        output += f"| {val}"
                    output = f"{output}"
                    print(output)

                connection.commit()

    def hapus_perangkat_dari_DB(self, id):
        with pymysql.connect(
            host="localhost",
            user="pbo",
            password="pbo",
            database="5220411272",
            cursorclass=pymysql.cursors.DictCursor,
        ) as connection:
            with connection.cursor() as cursor:
                sql = f"DELETE FROM in_ear_monitor WHERE id = {id};"
                cursor.execute(sql)
                connection.commit()



class HeadPhone(PerangkatAudio):
    def __init__(self, merek, harga, jack_audio, wireless, jenis):
        super().__init__(merek, harga, jack_audio, wireless)
        self.__jenis = jenis

    def get_jenis(self):
        return self.__jenis

    def tampilkan_detail(self):
        super().tampilkan_detail()
        print("Jenis Fitting: ", self.get_jenis())

    def tambah_perangkat_ke_DB(self):
        with pymysql.connect(
            host="localhost",
            user="pbo",
            password="pbo",
            database="5220411272",
            cursorclass=pymysql.cursors.DictCursor,
        ) as connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO headphone (merek, harga, jack_audio, wireless, jenis) VALUES (%s, %s, %s, %s, %s)"
                val = (
                    self.get_merek(),
                    self.get_harga(),
                    self._jack_audio,
                    self.wireless,
                    self.get_jenis(),
                )
                cursor.execute(sql, val)
                connection.commit()

    def tampilkan_tabel(self):
        with pymysql.connect(
            host="localhost",
            user="pbo",
            password="pbo",
            database="5220411272",
            cursorclass=pymysql.cursors.DictCursor,
        ) as connection:
            with connection.cursor() as cursor:
                sql = f"SELECT * FROM headphone;"
                cursor.execute(sql)
                rows = cursor.fetchall()

                output = ""
                for key, val in rows[0].items():
                    output += f"| {key}"
                print(output)
                print("-" * len(output))

                for row in rows:
                    output = ""
                    for key, val in row.items():
                        output += f"| {val}"
                    output = f"{output}"
                    print(output)

                connection.commit()

    def hapus_perangkat_dari_DB(self, id):
        with pymysql.connect(
            host="localhost",
            user="pbo",
            password="pbo",
            database="5220411272",
            cursorclass=pymysql.cursors.DictCursor,
        ) as connection:
            with connection.cursor() as cursor:
                sql = f"DELETE FROM headphone WHERE id = {id};"
                cursor.execute(sql)
                connection.commit()

    def tampilkan_satu_data(self, id):
        with pymysql.connect(
            host="localhost",
            user="pbo",
            password="pbo",
            database="5220411272",
            cursorclass=pymysql.cursors.DictCursor,
        ) as connection:
            with connection.cursor() as cursor:
                sql = f"SELECT * FROM headphone WHERE id = {id};"
                cursor.execute(sql)
                data = cursor.fetchone()
                if data:
                    output = ""
                    for k, v in data.items():
                        output += f"| {k}"
                    print(output)
                    output = ""
                    for k, v in data.items():
                        output += f"| {v}"
                    print(output)

                connection.commit()



# (merek, harga, jack_audio, wireless)
perangkat_audio_1 = PerangkatAudio("Sony a", 120_000, "3.5mm", False)
perangkat_audio_2 = PerangkatAudio("Sony b", 220_000, "3.5mm", False)
perangkat_audio_3 = PerangkatAudio("Sony v", 150_000, "4.4mm", True)
perangkat_audio_4 = PerangkatAudio("Sony z", 190_000, "4.4mm", False)
perangkat_audio_5 = PerangkatAudio("Sony y", 1_000_000, "3.5mm", True)

# (merek, harga, jack_audio, wireless, driver, detachable)
iem_1 = InEarMonitor("Samsung d", 4_000_000, "4.4", False, "planar", False)
iem_2 = InEarMonitor("Samsung f", 3_000_000, "6.4", False, "balance", False)
iem_3 = InEarMonitor("Samsung 3", 4_500_000, "4.4", True, "dinamis", True)
iem_4 = InEarMonitor("Samsung t", 5_000_000, "3.4", False, "planar", True)
iem_5 = InEarMonitor("Samsung y", 6_700_000, "2.2", True, "balance dinamis", True)

# (merek, harga, jack_audio, wireless, jenis):
hp_1 = HeadPhone("Xiaomi y", 1_000_000, "3.5mm", True, "over ear")
hp_2 = HeadPhone("Xiaomi d3", 1_000_000, "3.5mm", True, "bulat")
hp_3 = HeadPhone("Xiaomi g", 1_000_000, "3.5mm", True, "over ear")
hp_4 = HeadPhone("Xiaomi y4", 1_000_000, "3.5mm", True, "over ear")
hp_5 = HeadPhone("Xiaomi l0", 1_000_000, "3.5mm", True, "over ear")

semua_perangkat = [
    [
        perangkat_audio_1,
        perangkat_audio_2,
        perangkat_audio_3,
        perangkat_audio_4,
        perangkat_audio_5,
    ],
    [iem_1, iem_2, iem_3, iem_4, iem_5],
    [hp_1, hp_2, hp_3, hp_4, hp_5],
]
# Untuk menginputkan semua object ke DB dan menampilkannya
for perangkat in semua_perangkat:
    count = 5
    for unit in perangkat:
        unit.tampilkan_detail()
        print("=" * 75)
        print("")
        unit.tambah_perangkat_ke_DB()
        count -= 1
        if count == 0:
            unit.tampilkan_tabel()
            print("")

# update data
data_baru = {
    "merek": "Xiaomi Baru",
    "harga": 3_000_000,
    "jack_audio": "4.4mm",
    "jenis": "over ear"
}

print("Data hp_1 sebelum diperbarui: ")
hp_1.tampilkan_satu_data(1)
print()
hp_1.perbarui_detail_perangkat_di_DB(1, data_baru)
print("Data hp_1 setelah diperbarui: ")
hp_1.tampilkan_satu_data(1)
print()

print("Hasil qeury SELECT by id")
hp_1.tampilkan_satu_data(2)
print()
hp_1.tampilkan_satu_data(3)
print()
hp_1.tampilkan_satu_data(4)

tabel = ["perangkat_audio", "in_ear_monitor", "headphone"]
for perangkat in tabel:
    with pymysql.connect(
        host="localhost",
        user="pbo",
        password="pbo",
        database="5220411272",
        cursorclass=pymysql.cursors.DictCursor,
    ) as connection:
        with connection.cursor() as cursor:
            sql = f"DROP TABLE {perangkat};"
            cursor.execute(sql)
            connection.commit()


