croissantjesprijs = 0.39
stokbrodenprijs = 2.78
kortingsbonnenwaarde = 0.50
antalkortingsbonnen = 0
aantalcroissantjes = int(input("Hoeveel croissantjes wilt u?"))
print(aantalcroissantjes * croissantjesprijs)
aantalstokbroden = int(input("Hoeveel stokbroden wilt u?"))
print(aantalstokbroden * stokbrodenprijs)
aantalkortingsbonnen = input("Heeft u kortingsbonnen?")
if aantalkortingsbonnen == "ja":
    aantalkortingsbonnen = int(input("Hoeveel kortingsbonnen heeft u?"))



totaalbedrag = aantalcroissantjes * croissantjesprijs + aantalstokbroden * stokbrodenprijs
print(totaalbedrag - aantalkortingsbonnen * kortingsbonnenwaarde)
print("Wilt u contant of met uw pinpas betalen?")