def cylinderanswer():
    print("Ange höjden och radien på cylindern: ")
    height = input(str("Höjden: "))
    radius = input(str("Radien: "))
    cylinder = (math.pi * eval(radius) ** 2 * eval(height))
    print("Cylinderns volym är: " + str(cylinder) + "cm³")