from constraint import *

# variables for function
a = range(1,10)
b = 13
c = range(1,10)
d = range(1,10)
e = range(1,10)
f = 12
g = range(1,10)
h = range(1,10)
i = 11
j = range(1,10)
k = range(1,10)
l = range(1,10)
m = 10
n = 66

# variables for problem solver based on constraint package
problem = Problem()
problem.addVariable("a", range(1,10))
problem.addVariable("b", [13])
problem.addVariable("c", range(1,10))
problem.addVariable("d", range(1,10))
problem.addVariable("e", range(1,10))
problem.addVariable("f", [12])
problem.addVariable("g", range(1,10))
problem.addVariable("h", range(1,10))
problem.addVariable("i", [11])
problem.addVariable("j", range(1,10))
problem.addVariable("k", range(1,10))
problem.addVariable("l", range(1,10))
problem.addVariable("m", [10])
problem.addVariable("n", [66])

# main math function
def function1(a, b, c, d, e, f, g, h, i, j, k, l, m):
        return a + b * c / d + e + f * g - h - i + j * k / l - m

# constraint all range-set figures should be different from each other
problem.addConstraint(lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n: a != c and a != d and a != e and a != g and a != h and a != j and a != k and a != l and c != d and c != e and c != g and c != h and c != j and c != k and c != l and d != e and d != g and d != h and d != j and d != k and d != l and e != g and e != h and e != j and e != k and e != l and g != h and g != j and g != k and g != l and h != j and h != k and h != l and j != k and j != l and k != l)
problem.addConstraint(lambda a, b, c, d, e, f, g, h, i, j, k, l, m, n:
                      function1(a, b, c, d, e, f, g, h, i, j, k, l, m) == n)
                      
# show solution count and solutions   
print(len(problem.getSolutions()))
solutions = problem.getSolutions()
print(solutions)
