import random as rnd
class deste:
	def __init__(self):
		self.deste_kartsayisi = 52		
		self.turler = ["Karo","Kupa","Maça","Sinek"]
		#self.numaralar = ["A"]+[str(x) for x in range(2,11)]+["J","Q","K"]
		self.numaralar = ["A"]+list(map(lambda x : str(x),range(2,11)))+["J","Q","K"]
		self.deste = self.olustur()
		self.karistir()
		self.kes()
		#print(self.deste)

	def kes(self):
		r = rnd.randint(0,51)
		self.deste =  self.deste[r:] +self.deste[:r]

	def dagit(self, adet = 1):
		kartlar = []
		for _ in range(adet):
			kartlar.append(self.deste.pop())
		return kartlar

	def olustur(self):
# 		for z in self.turler:
# 			for y in self.numaralar:
# 				self.deste.append(z+y)
		return [x+y for x in self.turler for y in self.numaralar]

	def karistir(self):
		#rnd.sample(self.deste,52)
		rnd.shuffle(self.deste)


	def karistir1(self):
		liste = [0]*52
		for x in self.deste:
			r = rnd.randint(0,51)
			if liste[r] == 0:
				liste[r] = x
		return liste

	def karistir2(self): # hata var düzeltilecek
		liste = [0]*52
		x = 0

		while 0 in liste: #for x in range(52):
			r = rnd.randint(0,52)
			if liste[x]==0:
		
				liste[x] = self.deste[r]
				x += 1	
			#print("1.",liste,"\n",self.deste)
		return liste



#destem = deste()

#destem.olustur()