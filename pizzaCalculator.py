#comments René Rambow Pizza Calculator

priceSmall = 2.99
priceMedium = 4.99
priceLarge = 6.99

aantalSmall = int(input("Hoeveel small pizza's wilt u bestellen?"))
smallpizza = aantalSmall * priceSmall
print(smallpizza)
aantalMedium = int(input("Hoeveel medium pizza's wilt u bestellen?"))
mediumpizza = aantalMedium * priceMedium
print(mediumpizza)
aantalLarge = int(input("Hoeveel large pizza's wilt u bestellen?"))
largepizza = aantalLarge * priceLarge
print(largepizza)

totaal = smallpizza + mediumpizza + largepizza
print("U betaald voor uw bestelling")
print(totaal)