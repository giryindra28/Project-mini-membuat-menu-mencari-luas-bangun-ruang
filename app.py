

class bangun_ruang():
    def __init__ (self,a,b):
        self.a = a
        self.b = b

    def persegi(self):
        luas_persegi = self.a * self.b
        return print("Luas persegi adalah ", luas_persegi)    

    def luas_persegiPanjang(self):
        luas_persegipanjang = self.a * self.b
        return print("Luas persegi panjang = ",luas_persegipanjang)
    
    def luas_segitiga(self,c = 2):
        luas_segitiga = self.a * self.b / c
        return print("Luas segitiga = ", luas_segitiga)
    
    def belah_ketupat(self):
        luas_belahKetupat =  (self.a + self.b) * 0.5
        return print("Luas belah ketupat = ", luas_belahKetupat)
    
class lingkaran():
    def __init__ (self,jari_jari):
        self.jari_jari = jari_jari
    
    def luas_lingkaran(self, pi = 3.14):
        luas_Lingkaran = self.jari_jari **2 * pi
        return print("Luas lingkaran = ", round(luas_Lingkaran,2))

class sub_bangunRuang(bangun_ruang):
    def __init__ (self,a,b,c):
        bangun_ruang.__init__(self,a,b)
        self.c = c
    
    def luas_trapesium(self, setengah = 1/2):
        luas_trapesium = setengah * (self.a + self.b) * self.c
        return print("Luas trapesium adalah = ", luas_trapesium)

    def luas_balok(self):
        luas_balok = 2*(self.a * self.b) + 2*(self.a*self.c) + 2*(self.b*self.c)
        return print("Luas balok adalah =", luas_balok)

