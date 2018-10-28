#Brings in all the mathematics code that I will be using
import math


#Finds the resultant vector given the magnitude of them and the angke between them
def Resultant():
    #Takes in the magnitudes of the vectors and the angle between them
    F_1 = int(input("What is the force of the " + '\x1b[0;30;42m' + 'first vector' + '\x1b[0m' + " in " + '\x1b[0;30;44m' + 'Newtons' + '\x1b[0m' + "?\n"))
    F_2 = int(input("What is the force of the " + '\x1b[0;30;42m' + 'second vector' + '\x1b[0m' + " in " + '\x1b[0;30;44m' + 'Newtons' + '\x1b[0m' + "?\n"))
    theta = int(input("What is the " + '\x1b[0;30;42m' + 'angle' + '\x1b[0m' + " between the two vectors in  " + '\x1b[0;30;44m' + 'degrees' + '\x1b[0m' + "?\n"))
    #Cosines only takes in radians, so I have to convert from degrees to radians
    rad = math.radians(theta)
    #Law of Cosines formula
    k = (F_1)**2 + (F_2)**2 - 2 * F_1 * F_2 * math.cos(rad)
    Ans = math.sqrt(k)
    #Prints the magnitude of the force of the resultant vector
    print("The force of the resultant vector is %s Newtons."%(Ans))

def Area_Triangle_Vectors():
    #Takes in the x, y, and z coordinates of the three points of the triangle in the xyz space
    x_1 = int(input("What is " + '\x1b[0;30;42m' + 'x-coordinate' + '\x1b[0m' + " of " + '\x1b[0;30;44m' + 'point A' + '\x1b[0m' + "?\n"))
    y_1 = int(input("What is " + '\x1b[0;30;42m' + 'y-coordinate' + '\x1b[0m' + " of " + '\x1b[0;30;44m' + 'point A' + '\x1b[0m' + "?\n"))
    z_1 = int(input("What is " + '\x1b[0;30;42m' + 'z-coordinate' + '\x1b[0m' + " of " + '\x1b[0;30;44m' + 'point A' + '\x1b[0m' + "?\n"))
    x_2 = int(input("What is " + '\x1b[0;30;42m' + 'x-coordinate' + '\x1b[0m' + " of " + '\x1b[0;30;44m' + 'point B' + '\x1b[0m' + "?\n"))
    y_2 = int(input("What is " + '\x1b[0;30;42m' + 'y-coordinate' + '\x1b[0m' + " of " + '\x1b[0;30;44m' + 'point B' + '\x1b[0m' + "?\n"))
    z_2 = int(input("What is " + '\x1b[0;30;42m' + 'z-coordinate' + '\x1b[0m' + " of " + '\x1b[0;30;44m' + 'point B' + '\x1b[0m' + "?\n"))
    x_3 = int(input("What is " + '\x1b[0;30;42m' + 'x-coordinate' + '\x1b[0m' + " of " + '\x1b[0;30;44m' + 'point C' + '\x1b[0m' + "?\n"))
    y_3 = int(input("What is " + '\x1b[0;30;42m' + 'y-coordinate' + '\x1b[0m' + " of " + '\x1b[0;30;44m' + 'point C' + '\x1b[0m' + "?\n"))
    z_3 = int(input("What is " + '\x1b[0;30;42m' + 'z-coordinate' + '\x1b[0m' + " of " + '\x1b[0;30;44m' + 'point C' + '\x1b[0m' + "?\n"))
    #Finds two vectors of the triangle
    AB_x = x_2 - x_1
    AB_y = y_2 - y_1
    AB_z = z_2 - z_1
    AC_x = x_3 - x_1
    AC_y = y_3 - y_1
    AC_z = z_3 - z_1
    #Finds the cross product of the two vectors
    cross_x = AB_y * AC_z - AB_z * AC_y
    cross_y = AB_z * AC_x - AC_z * AB_x
    cross_z = AB_x * AC_y - AC_x * AB_y
    #Finds the magnitude of the cross product and then takes half of it to find the area
    Mag = math.sqrt((cross_x)**2 + (cross_y)**2 + (cross_z)**2)
    Area = .5 * Mag
    #Prints the area
    print("The area of the triangle determined by those three points is %s."%(Area))

#Finds the measure of the acute angle between two lines on the coordinate plane
def Angle_Two_Lines():
    #Asks for the direction vectors of the line
    a_d1 = int(input("What is " + '\x1b[0;30;42m' + 'x-component' + '\x1b[0m' + " of the direction vector of the " + '\x1b[0;30;44m' + 'first' + '\x1b[0m' + " line?\n"))
    b_d1 = int(input("What is " + '\x1b[0;30;42m' + 'y-component' + '\x1b[0m' + " of the direction vector of the " + '\x1b[0;30;44m' + 'first' + '\x1b[0m' + " line?\n"))
    a_d2 = int(input("What is " + '\x1b[0;30;42m' + 'x-component' + '\x1b[0m' + " of the direction vector of the " + '\x1b[0;30;44m' + 'second' + '\x1b[0m' + " line?\n"))
    b_d2 = int(input("What is " + '\x1b[0;30;42m' + 'y-component' + '\x1b[0m' + " of the direction vector of the " + '\x1b[0;30;44m' + 'second' + '\x1b[0m' + " line?\n"))
    Mag_1 = math.sqrt((a_d1)**2 + (b_d1)**2)
    Mag_2 = math.sqrt((a_d2)**2 + (b_d2)**2)
    #Takes the dot product
    Dot_Product = math.fabs(a_d1 * a_d2 + b_d1 * b_d2)
    #Uses the formula
    Cosine = Dot_Product / (Mag_1 * Mag_2)
    #Takes the reverse cosine and then converts to degrees
    k = math.acos(Cosine)
    Ans = math.degrees(k)
    #Prints the number of degrees
    print("The angle between the two lines is %s degrees."%(Ans))

#Finds the distance from a point on the coordinate plane to a line on 2D space
def Distance_Point_Line():
    print("Note: Your equation for your line must be in the form Ax + By + C = 0 where A, B, and C are real numbers.")
    #Takes in inputs (the coordinates of the points and details about the line's equation)
    A = int(input("What is " + '\x1b[0;30;42m' + 'A' + '\x1b[0m' + " in your equation for your " + '\x1b[0;30;44m' + 'line' + '\x1b[0m' + "?\n"))
    B = int(input("What is " + '\x1b[0;30;42m' + 'B' + '\x1b[0m' + " in your equation for your " + '\x1b[0;30;44m' + 'line' + '\x1b[0m' + "?\n"))
    C = int(input("What is " + '\x1b[0;30;42m' + 'C' + '\x1b[0m' + " in your equation for your " + '\x1b[0;30;44m' + 'line' + '\x1b[0m' + "?\n"))
    x = int(input("What is the " + '\x1b[0;30;42m' + 'x-coordinate' + '\x1b[0m' + " of your " + '\x1b[0;30;44m' + 'point' + '\x1b[0m' + "?\n"))
    y = int(input("What is the " + '\x1b[0;30;42m' + 'y-coordinate' + '\x1b[0m' + " of your " + '\x1b[0;30;44m' + 'point' + '\x1b[0m' + "?\n"))
    #Plugs the information into a complicated formula
    numerator = math.fabs(A * x + B * y + C)
    denominator = math.sqrt(A**2 + B**2)
    Ans = numerator / denominator
    #Prints the distance
    print("The distance from the point to the line is %s."%(Ans))

#These messages display when the program is runned.
#The keys on the keyboard that are involved are highlighted in red, so that it is easier for the viewer to see it
print("Welcome to Vector Calculations Beta Version.")
print("If you would like to find the resultant vector of two vectors, type " + '\x1b[0;30;41m' + '1' + '\x1b[0m' + ".")
print("If you would like to find the area of a triangle given its three points in 3D space, type " + '\x1b[0;30;41m' + '2' + '\x1b[0m' + ".")
print("If you would like to find the angle between two lines, type " + '\x1b[0;30;41m' + '3' + '\x1b[0m' + ".")
print("If you would like to find the distance between a point and a line, type " + '\x1b[0;30;41m' + '4' + '\x1b[0m' + ".")
Option = int(input("Choose one of those features by typing the appropriate number and then pressing " + '\x1b[0;30;41m' + 'Enter' + '\x1b[0m' + ".\n"))

#Chooses the appropriate function based on the user input

if Option == 1:
    Resultant()

if Option == 2:
    Area_Triangle_Vectors()

if Option == 3:
    Angle_Two_Lines()

if Option == 4:
    Distance_Point_Line()
