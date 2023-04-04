class oyuncu:

	def __init__(self, ad=" "):
		self.oyuncu_adi = ad
		self.oyuncu_puan = 0
		self.oyuncu_kartlar = []
		self.pisti = 0
		self.para  = 0
		self.toplanan_kartlar = []




	def kart_at(self, kartlar_idx):
		atilacak = []
		kartlar_idx.sort(reverse=True)
#		kartlar_idx.reverse()
		for _ in kartlar_idx:
			atilacak.append(self.oyuncu_kartlar.pop(_))
		return atilacak


# oyuncu1 = oyuncu()

# atilsin = oyuncu1.kart_at([0,3,2,1])

# print(atilsin)