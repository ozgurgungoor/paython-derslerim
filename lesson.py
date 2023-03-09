print("""Merhaba
Dünya


!!!""")


print("Merhaba \nDünya")

print("Merhaba \t\t\tDünya")

mesaj = "Merhaba dünyaa "

mesaj2 = "Merhaba dünyaa"

print(mesaj +" "+ mesaj2)

print(mesaj2[0:7])


print("merhaba " * 10)




isim = "Özgür"

yas = "19"

print("{} , {} yaşındadır".format(isim,yas))





mesaj3 = "Üniversiteliyim"

print("{} , {} dedi...".format(isim,mesaj3)) 



print("Merhaba \n \t \t \t Merhaba")



print(f"{isim} {mesaj} dedi")



 
plaka=input('Plaka Girin :')
 
cikti = ''
if plaka == '06':
  cikti = 'Ankara'
elif plaka == '07':
  cikti = 'Antalya'
elif plaka == '08':
  cikti = 'Artvin'
elif plaka == '11':
  cikti = 'Kahramankazan'
else:
  cikti = 'Türkiye'
 
print(cikti)