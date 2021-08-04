#99 bottles of beer on the wall, 99 bottles of beer
#Take one down and pass it around, 98 bottles of beer on the wall
#.....
#1 bottle of beer on the wall, 1 bottle of beer.
#Go to the store and buy some more, 99 bottles of beer on the wall.
b = list(range(1,100))
a=list(reversed(b))

def print_on_terminal (j):
    if j == 99:
        for i in a[0:j-1]:
            print(i, " bottles of beer on the wall, ",i, " bottles of beer")
            if i == 2 :
                print("Take one down and pass it around, ",i-1," bottle of beer on the wall")
                print("")
                print("{} bottle of beer on the wall, {} bottle of beer".format(i-1,i-1))
            else:
                print("Take one down and pass it around, ",i-1," bottles of beer on the wall")
                print("")
        print("Go to the store and buy some more, {} bottles of beer on the wall.".format(a[0]))
        print("")
    elif j <99:
        for i in a[0:j]:
            print(i, " bottles of beer on the wall, ",i, " bottles of beer")
            print("Take one down and pass it around, ",i-1," bottles of beer on the wall")
            print("")
    else:
        print("Only enter the max number of iterations is 99 ! ")

def print_on_txt (e):
    txt = open('botles_new.txt', 'w')   
    if e == 99 :
        for i in a[0:e]:
            txt.write("{} bottles of beer on the wall, {} bottles of beer\n".format(i,i))
            if i == 2 :
                txt.write("Take one down and pass it around, {} bottle of beer on the wall\n".format(i-1))
                txt.write("\n")
                txt.write("{} bottle of beer on the wall, {} bottle of beer\n".format(i-1,i-1))
            else:
                txt.write("Take one down and pass it around, {} bottles of beer on the wall\n".format(i-1))
                txt.write("\n")
            txt.write("Go to the store and buy some more, {} bottles of beer on the wall.".format(a[0]))
    elif e < 99 :
        for i in a[0:e]:
            txt.write("{} bottles of beer on the wall, {} bottles of beer\n".format(i,i))
            txt.write("Take one down and pass it around, {} bottles of beer on the wall\n".format(i-1))
            txt.write("\n")
    else :
        txt.write("You only enter the max number of iterations is 99 !\n")

x= int(input("Enter your choise _ 0/1 : "))
if x == 0:
    y = 99
    z = str(input("Do you want write to txt _ y/n : "))
    if z == 'y' :
        print_on_terminal(y)
        print_on_txt(y)
    elif z == 'n':
        print_on_terminal(y)
    else:
        print("Only enter y or n !")
elif x ==1 :
    n = int(input("Enter number of iterations : "))
    z = str(input("Do you want write to txt _ y/n : "))
    print("")
    if z == 'y' :
        print_on_terminal(n)
        print_on_txt(n)
    elif z == 'n':
        print_on_terminal(n)
    else:
        print("Only enter y or n !")
else :
    print("You only allow to enter 0 or 1 !")





            




