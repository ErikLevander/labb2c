import math

count = 0





def cubeanswer():
    side = input(str("Ange sidans längd på kuben i centimeter: \n"))
    cube = float(side) ** 3
    print("Kubens volym är " + str(cube) + " cm³")
    

def tetraanswer():
    tside = input(str("Ange sidan längd på tetrahedronen: \n"))
    rot = math.sqrt(2)
    tetra = (float(tside) ** 3) / (6 * float(rot))
    print("Tetrahedronens volym är: " + str(tetra) + " cm³")

def bmianswer():
    height = input(str("Ange din längd i meter: "))
    weight = input(str("Ange din vikt i kilo: "))
    bmi = (float(weight)) / ((float(height) ** 2))
    print("Ditt bmi är: " + str(bmi))

def cylinderanswer():
    print("Ange höjden och radien på cylindern: ")
    height = input(str("Höjden: "))
    radius = input(str("Radien: "))
    cylinder = (math.pi * eval(radius) ** 2 * eval(height))
    print("Cylinderns volym är: " + str(cylinder) + "cm³")


def menu():
    print('\n\n========================================')
    print('|            Vad vill du göra?         |')
    print('|                                      |')
    print('|  1. Beräkna volymen på en kub        |')
    print('|  2. Beräkna volymen på en tertahedron|')
    print('|  3. Beräkna ditt bmi                 |')
    print('|  4. Beräkna volymen på en cylinder   |')
    print('|  5. Avsluta                          |')
    print('========================================')
    


while True:
    menu()
    choice = input('Gör ditt val: ')
    if choice == "1":
        cubeanswer()
        count += 1
    elif choice == "2":
        tetraanswer()
        count += 1   
    elif choice == "3":
        bmianswer()
        count +=1
    elif choice == "4":
        cylinderanswer()
        count +=1
    elif choice == "5":
        print(f'Du har gjort {count} beräkningar. Välkommen tillbaka')
        break
    else:
        print('\n -----> Försök igen <-----')