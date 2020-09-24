



print ("Och se, din son ska heta...")
namn = input("Ja, vad heter du själv? ")
sonnamn = namn+"son"
print ("Och se, din son ska heta", sonnamn)


pnr = input("Personnummer: ")
if len(pnr)==11:
    pnr = pnr[0:6]+pnr[7:]

if pnr[6]=="-":
    year = pnr[0:2]
    year = int(year)
    year += 1900

n = 1

n = (" "+str(n))
l = (len(n))
print (n[-8:l])
