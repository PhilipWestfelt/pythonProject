x = input("Din längd (cm): ")
y = float(x)*0.01
def idealvikt(langd):
    global x
    x = 0
    vikt = 23 * langd * langd
    return vikt
print ("Idealvikt:", idealvikt(y))










