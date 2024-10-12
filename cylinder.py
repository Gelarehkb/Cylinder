radius = float(input('Radius (in metres): '))
height = float(input('Height (in metres): ')) 
pi = 3.14159

surface = pi*(radius**2)
exterior = 2*pi*radius*height
surfaces = float((2*surface) + exterior) #1
volume = float(surface * height) #2
waterNeed = float(0.9 * volume) #3
paintNeed = float(surfaces * 0.65) #4
platesNeed = int(surfaces//2) + 1

print(f'Surface area of the tank: {surfaces:.2f}')
print(f'Volume of the tank: {volume:.2f}')
print(f'Amount of water needed: {waterNeed:.2f}')
print(f'Litres of paint needed: {paintNeed:.2f}')
print(f'Number of plates needed: {platesNeed}')
