# Create a program that calculates the area of a triangle (1/2 * base* height)
# The base and height should be entered using the keyboard.
# SOLUTION
triangle_height = int(input("Enter the height value: "))
triangle_base = int(input("Enter the base value: "))
triangle_area = (1/2)* triangle_base * triangle_height
print(f"The area of the triangle with base {triangle_base} and height {triangle_height} is {triangle_area:.0f}")