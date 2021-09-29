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

print("""------------------""")
print(f'{aantalSmall} Small voor {priceSmall} per pizza ' + str(aantalSmall*priceSmall))
print(f'{aantalMedium} Medium voor {priceMedium} per pizza ' + str(aantalMedium*priceMedium))
print(f'{aantalLarge} Large voor {priceLarge} per pizza ' + str(aantalLarge*priceLarge))
print(f'U betaald totaal' + str(totaal))
print("""------------------""")