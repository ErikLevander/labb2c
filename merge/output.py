def cylinderanswer():
    print("Ange höjden och radien på cylindern: ")
    height = input(str("Höjden: "))
    radius = input(str("Radien: "))
    cylinder = (math.pi * eval(radius) ** 2 * eval(height))
    print("Cylinderns volym är: " + str(cylinder) + "cm³")


def bmianswer():
    height = input(str("Ange din längd i meter: "))
    weight = input(str("Ange din vikt i kilo: "))
    bmi = (float(weight)) / ((float(height) ** 2))
    print("Ditt bmi är: " + str(bmi))


def tetraanswer():
    tside = input(str("Ange sidan längd på tetrahedronen: \n"))
    rot = math.sqrt(2)
    tetra = (float(tside) ** 3) / (6 * float(rot))
    print("Tetrahedronens volym är: " + str(tetra) + " cm³")


