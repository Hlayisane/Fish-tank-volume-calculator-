import math, random

#tell user how the program funtions/alert them on what they should do

name =input("Enter your name: (leave empty to exit) ")

if name!="":
    print("\n\tMenu")
    print("\t1. Calculation of the volume of the fish tank")
    print("\t2. Display info")
    print("\t3. Discount")

    selected=int(input("\n\tSelect your menu item: "))


#while name is not empty
while name !="":
    if selected==1:
        print("Fish tank volume calculation")
        Shape=input("What is the shape of the tank? Cube(cu)/Sphere(sp): ")
        if Shape=="cu":
            side=float(input("what is the side of the cube? (cm) : "))
            TankVolume=math.pow(side,3)
        elif Shape=="sp":
            diameter=float(input("What is thediameter of the sphere? : (cm)"))
            TankVolume=4/3*math.pow(diameter/2,3)

        print("\nThe volume of the fish tank is \t"+str(round(TankVolume,0))+"mlvolume")
        print("\nThe tank can hold \t"+str(round(TankVolume/1000,1))+"liters of water")
        
    elif selected==2:
         print("\nFeed your fish")
         print("Dont't OVERFEED your fish")

    elif selected==3:
        print(name + ", your dicount is: "+ str(random.randint(1,10))+ "%")


    else:
        print(name, "\nThats not a valid menu item")


    name =input("\nEnter your name: (leave empty to exit) ")

    if name!="":
        print("\n\tMenu")
        print("\t1. Calculation of the volume of the fish tank")
        print("\t2. Display info")
        print("\t3. Discount")
        selected = int(input("\tSelect your menu item: "))


input("Press enter to exit")
exit()
