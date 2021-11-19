def PrintRectangle(a, b, file):
    f = open(file, "w")
    for i in range(a):
        f.write("*")
        f.write(" ")
    f.write("\n")
    for j in range(b - 2 ):
        f.write("*")
        for k in range(a + (a - 3) ):
            f.write(" ")
        f.write("*")
        f.write("\n")
    for i in range(a):
        f.write("*")
        f.write(" ")


    f.close()


def PrintSquare(a, file):
    f = open(file, "w")

    for i in range(a):
        f.write("*")
        f.write(" ")
    f.write("\n")
    for j in range(a - 2 ):
        f.write("*")
        for k in range(a + (a - 3) ):
            f.write(" ")
        f.write("*")
        f.write("\n")
    for i in range(a):
        f.write("*")
        f.write(" ")

    f.close()