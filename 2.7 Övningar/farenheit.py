def fahrenheit(C):
    f = 32.0 +float(C) * 1.8
    return f

print ("Temperatur (grader C): ")
x = input()
y = fahrenheit(x)

print ("Alltså", y, "grader F")