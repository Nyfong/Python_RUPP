import math
print("Exercise")
print('*'*20)
title_list = ["BMI","Area Of Circle","Area Of Triangle"] #stored title in list
#exercise 1
print( len(title_list)-2, title_list[-3] )
user_weight = float(input("Fill your Weight:"))
user_height = float(input("Fill your Height in meters:"))
user_bmi = user_weight / pow(user_height, 2)
print("your BMI:%.2f" %user_bmi)
#exercise 2
print( len(title_list)-1, title_list[-2] )
input_radius = float(input("Fill the raduis:"))
ans_circle = math.pi* pow(input_radius, 2)
print("Area of circle:%.3f" %ans_circle)
#exercise 3
print( len(title_list), title_list[-1] )
input_width = float(input(""))
input_height = float(input(""))
ans_triangle = 0.5 * input_height * input_width
print("Area of triagle:", ans_triangle)

'''
#1
def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi
weight = float(input("Enter your weight in kilograms: "))

height = float(input("Enter your height in meters: "))
bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi:.2f}")
import math
#2
def calculate_circle_area(radius):
    """Calculate the area of a circle given the radius."""
    area = math.pi * radius ** 2
    return area
radius = float(input("Enter the radius of the circle: "))
area = calculate_circle_area(radius)
print(f"The area of the circle is: {area:.2f}")
#3
def calculate_triangle_area(base, height):
    """Calculate the area of a triangle given the base and height."""
    area = 0.5 * base * height
    return area
base = float(input("Enter the base of the triangle: "))

height = float(input("Enter the height of the triangle: "))
area = calculate_triangle_area(base, height)
print(f"The area of the triangle is: {area:.2f}")
'''