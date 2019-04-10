
#2 Cartesian Product
def Cartesianify(x,y):
    for val_x in x:
        for val_y in y:
            print (val_x, val_y)

#Test case
x = ('a', 'e')
y = (1,3,7,9)
Cartesianify(x,y)
input("Press Enter to continue...")