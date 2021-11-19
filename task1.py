from task1_module import PrintRectangle
from task1_module import PrintSquare

dlina = input().split(" ")
file = input()
file = file.strip("\"\'")  # Удаляем ковычки

if len(dlina) == 1:
    PrintSquare(int(dlina[0]), file)
elif len(dlina) == 2:
    PrintRectangle(int(dlina[0]), int(dlina[1]), file)