import random

print ("Hello World")


'''
Step 1: Initialise x0 and y0
'''

print("Step 1: Initialise x0 and y0")
print("x0 and y0 are assigned a pseudorandom integer between 0 and 99 inclusive")

#x0 = 50
#y0 = 50

x0 = random.randint(0,99)
y0 = random.randint(0,99)

print("x0", x0)
print("y0", y0)

'''
Step 2: Move x0 and y0
'''

print("Step 2: Move x0 and y0")

#Initialise a random number between 0 and just less than 1

random_number = random.random()

#Print("random_number", random_number)

if random_number < 0.5:
    x0 += 1 # equivallent to "x0 = x0 + 1"

else:
    x0 += 1

print("New location of x0: ", x0)

#Get next random number

random_number = random.random()

#Print("random_number", random_number)

if random_number < 0.5:
    y0 += 1

else:
    y0 -= 1

print("New location of y0: ", y0)

'''
Step3: Initialise second set of points: x1 and y1
'''

print("Initialise x1 and y1")
print("x1 and y1 are assigned a pseudorandom integer between 0 and 99 inclusive")

x1 = random.randint(0,99)
y1 = random.randint(0,99)

print("x1", x1)
print("y1", y1)

'''
Step 4: Move x1 and y1
'''

print("Step 4: Move x1 and y1")

#Get next random number

random_number = random.random()

#Print("random_number", random_number)

if random_number < 0.5:
    x1 += 1
    print("x1 += 1")
else:
    x1 -= 1
    print("x1 -= 1")

print("New location of x1: ", x1)

#Get next random number

random_number = random.random()

#Print("random_number", random_number)

if random_number < 0.5:
    y1 += 1

else:
    y1 -= 1

print("New location of y1: ", y1)

'''
Step 5: Calculate and print distance between coordinates (x0, y0) and (x1, y1)
        using Pythagoras theorem
'''

print("Step 5: Calculate and print distance between coordinates (x0, y0) and (x1, y1)")
print("using Pythagoras theorem")

distance = ((x0 - x1)**2 + (y0 - y1)**2)**0.5
print("distance ",distance)