from typing_extensions import Self


class Hewan:
    nama_latin = ''
    def __init__(Self, nama, umur):
        Self.nama_latin = nama
        Self.umur = umur
    
    @classmethod
    def change_nama_latin(cls, nama, umur):
        print("check")
        return cls(nama, umur)
    
    def bangun():
        print("Hoaaammmmm")

    def display():
        print("nama latin :" + Self.nama_latin)

class Kucing(Hewan):

    def bangun():
        print("Meowwww")

    def set_lari(kecepatan):
        speed = kecepatan
        if speed > 10:
            print("cepat sekali")
        else:
            print("lambat")

# obj1 = Hewan
obj2 = Kucing
obj2.change_nama_latin("spinx", 5)

print("nama latin nya : " + obj2.nama_latin)
obj2.display
speed = obj2.set_lari(15)