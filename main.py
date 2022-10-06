from my_module import circumference, square_footage

operation = input("Type 'circle' for circumference, or 'square' for square footage").lower()

if operation == 'circle':
    radius = input("What is the radius?: ")
    circumference(radius)
    
if operation == 'square':
    length = input("What is the length?: ")
    width = input("What is the width?: ")
    square_footage(length, width)

