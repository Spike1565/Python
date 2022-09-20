#Question 1
from cmath import pi
from math import radians


#radius = float(input('Please enter the circle radius:'))
pi = 3.14159
area = pi*radius**2
print ('You entered',radius, 'the area of circle is' ,area,)

#Question 2
farenhiet = float(input('Please enter the temperature in Farenheit))
celcius = (farenheit - 32) * 5/9
print (farenhiet,'Farenheit in Celcius is',celcius)

#Question 3
num_1 = int(input('Please enter the first number:'))
num_2 = int(input('Please enter the second number:'))
print ('The sum of' + str(num_1) +' and ' + str(num_2) +' is ' + str(num_1 + num_2))

#Question 4
num_1 = int(input('Please enter the first number:'))
num_2 = int(input('Please enter the second number:'))
product = num_1 * num_2
print ('The product of' ,num_1, 'and' ,num_2, 'is' ,product,)

#Question 5
total_slices = 4 * 4
number_of_pizzas = (total_slices + 5)//6
slices_left = number_of_pizzas * 6 - total_slices
print ('Number of pizzas required is',number_of_pizzas,'there will be',slices_left,'remaining slices.')
