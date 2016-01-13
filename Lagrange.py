from sympy import *
import numpy as np
'''
x = Symbol('X')
z = Symbol('Z')
y = (x*z)**2
yprime = y.diff(x)
print yprime

f = lambdify(x, yprime, 'numpy')

print f(5)
'''
def one_side(eq):
	eq = list(eq)
	i = 0
	bit = 0
	for char in eq:
		if char == '=':
			eq[i] = '-'
			bit = 1
		if bit == 1:
			if char == '+':
				eq[i] = '-'
			if char == '-':
				eq[i] = '+'
		i += 1
	return "".join(eq)

def lagrange(all_parameters, choice_vars, obj_fun, constraints):
	L = obj_fun
	i = 0
	FOCs = []
	for fun in constraints:
		temp = "l%d" %i
		exec(temp + "= Symbol('%s')" %temp)
		L += "-%s" %temp + "*(" + one_side(fun)  + ")"
		i+=1
	for var in all_parameters:
		temp = var
		exec(var + "= Symbol('%s')" %var)
	L = eval(L)
	print L
	for var in choice_vars: 
		deriv = L.diff(var)	
		print deriv
		'''
		METHOD:
		Set up lagrangian.
		Take FOCs.
		Solve for choice variables.
		Look at solver function in sympy.
		'''
	return L

print lagrange(["x", "y", "a", "b", "c"], ["x", "y", "c"], "a*x+b*y", ["20*c = 9", "2*x + 9 = 4"])
#print eval('c +2')
