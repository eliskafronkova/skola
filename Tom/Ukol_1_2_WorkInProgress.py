#2, podle datumu (den.mesic) ti program najde znameni zverokruhu (hledame jen ve 3 znamenich býk, beran, blizenci)

#Beran     20.3. - 20.4.
#Býk       20.4. - 21.5.
#Blíženci  22.5. - 21.6.

den = 18
mesic = 5

class znameni:
    def __init__(self, jmeno, denZ, denK, mesicZ, mesicK):
        self.jmeno = jmeno
        self.den_Z = denZ
        self.den_K = denK
        self.mesic_Z = mesicZ
        self.mesic_K = mesicK

    def getDenZ(self):
        return self.den_Z

    def getDenK(self):
        return self.den_K

    def getMesicZ(self):
        return self.mesic_Z 

    def getMesicK(self):
        return self.mesic_K


beran = znameni("Beran", 20, 20, 3, 4)
byk = znameni("Býk", 20, 21, 4, 5)
blizenci = znameni("Blíženci", 22, 21, 5, 6)

Znameni = [beran, byk, blizenci]

ZnameniM = []

for i in Znameni:
    if mesic == i.getMesicZ or mesic == i.getMesicK:
        ZnameniM.append(i)

