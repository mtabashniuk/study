import math

a = float(input("Введіть довжину а: "))
b = float(input("Введіть довжину b: "))
c = float(input("Введіть довжину c: "))
half_perimeter = (a + b + c) / 2
square = math.sqrt(
    half_perimeter * (half_perimeter - a) * (half_perimeter - b) * (half_perimeter - c)
)
print(square)