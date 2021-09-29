toegangsticket = 7.45
gameseattijd = 5
gameseatprijs = 0.37

aantalpersonen = int(input("Hoeveel kaartjes wilt u kopen?"))
print(aantalpersonen * toegangsticket)

gameseat = int(input("Hoeveel minuten wilt u in de gameseat?"))
print(gameseat / gameseattijd * gameseatprijs)

totaalbedrag = aantalpersonen * toegangsticket + gameseat / gameseattijd * gameseatprijs
print(totaalbedrag)

print("Wilt u contant of met uw pinpas betalen?")