import sympy

x,y = sympy.Symbol('x, y')

f = x**2 + sympr.exp(y**2)

f_prime = f.diff(x)

f_prime_func = lambdify((x,y), f_prime)

print(f_prime_func(1,2)) # calculate f_prime with x == 1 && y == 2


