def bmianswer():
    height = input(str("Ange din längd i meter: "))
    weight = input(str("Ange din vikt i kilo: "))
    bmi = (float(weight)) / ((float(height) ** 2))
    print("Ditt bmi är: " + str(bmi))