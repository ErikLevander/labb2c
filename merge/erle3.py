def tetraanswer():
    tside = input(str("Ange sidan längd på tetrahedronen: \n"))
    rot = math.sqrt(2)
    tetra = (float(tside) ** 3) / (6 * float(rot))
    print("Tetrahedronens volym är: " + str(tetra) + " cm³")