from constraint import *
import numpy as np

# Set input for T: 0 < T <= 1000
T = int(input("Please specify total units to sell(T): "))
while T > 1000 or T <= 0:
    T = int(input("Please specify total units to sell(T) 0 < T <= 1000: "))

# Set input for D: 0 < D <= 200
D = int(input("Please specify number of days(D): "))
while D > 200 or D <= 0:
    D = int(input("Please specify total number of days(D) 0 < D <= 200: "))

# Set input for Di: 0 < Di <= 200
Di = []
day = 1
z = 1
while len(Di) < D:
    z = int(input(f"Set a maximum number of units you can sell for the {day} day(Di): "))
    while z > 200 or z <= 0 or z =='':
        z = int(input(f"Set a maximum number of units you can sell for the {day} day(Di), 0 < D(i) <= 200: "))
    else:
        Di.append(z)
        day += 1
else:
    pass

# set problem and variables
x = 1
problem = Problem()
for i in Di:
    problem.addVariables((["day"+str(x)]), range(1,i+1))
    x+=1
# set main constraint (sum(Di)) == T
problem.addConstraint(ExactSumConstraint(T))

# print out the results - number of possible solutions
print(f'Possible solutions:')
print(len(problem.getSolutions()))
# print out all the possible solutions
print(f'Solutions:')
solution = np.array(sorted(sorted(y.items()) for y in problem.getSolutions()))
print(solution)
