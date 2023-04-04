import deste
import oyuncu
enson = 1
def kontrol_et(ikikart,adet):
	if adet>1:
		if (ikikart[0][-1] == ikikart[1][-1]) and (ikikart[0][-1] == "J") and (adet==2):
				return "J Pişti"
		elif (ikikart[0][-1] == ikikart[1][-1]) and (ikikart[0][-1] != "J"):
			if adet>2:
				return "Topla"
			else:
				return "Pişti"
		elif (ikikart[0][-1] != ikikart[1][-1]) and (ikikart[1][-1] == "J"):
			return "Topla"
		else:
			return "devam"

isimler = ["Ali","Veli","Ayşe","Fatma"]

destem = deste.deste()


#oyuncular = []
# yöntem 1
# for sirano in range(4):
# 	oyuncular.append(oyuncu.oyuncu("oyuncu "+str(sirano)))

# for pistioyuncusu in oyuncular:
# 	print(pistioyuncusu.oyuncu_adi)

# yöntem 2
# for isim in isimler:
# 	oyuncular.append(oyuncu.oyuncu(isim))
# for pistioyuncusu in oyuncular:
#  	print(pistioyuncusu.oyuncu_adi)

#yöntem 3
#oyuncular = [ oyuncu.oyuncu(isimler[_]) for _ in range(4)]

#yöntem 4
oyuncular = [ oyuncu.oyuncu(isim) for isim in isimler]





yer = destem.dagit(4)



for tur in range(3):
	for oyuncu in oyuncular:
		oyuncu.oyuncu_kartlar = destem.dagit(4)

	for tur1 in range(4):
		for oyuncu in oyuncular:
			yer.append(oyuncu.kart_at([3-tur1])[0])
			print(yer[-1])
			sonuc = kontrol_et(yer[-2:],len(yer))

			if sonuc == "J Pişti":
				oyuncu.pisti += 2
				oyuncu.toplanan_kartlar += yer
				yer = []
				enson = oyuncu
			elif sonuc == "Pişti":
				oyuncu.pisti += 1
				oyuncu.toplanan_kartlar += yer
				yer = []
				enson = oyuncu
			elif sonuc == "Topla":
				oyuncu.toplanan_kartlar += yer
				yer = []
				enson = oyuncu
			else:
				pass
enson.toplanan_kartlar += yer
yer = []

for oyuncu in oyuncular:
	print(oyuncu.toplanan_kartlar, oyuncu.pisti)

print(yer, destem.deste)			


 

