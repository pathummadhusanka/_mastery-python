"""
Consider the code snippet:

# def divide(a, b):
# 	return a / b

# print(divide(2, 4))

# print(divide(4, 2))

Output:
0.5
2.0

Requirement: Always divide bigger number by smaller number,
using decorator feature.
"""

# def greater_first(func):
# 	def wrap(a, b):
# 		if a < b:
# 			a, b = b, a
# 		return func(b, a)
# 	return wrap

# @greater_first
# def divide(a, b):
# 	return a / b

# print(divide(2, 4))

# print(divide(4, 2))

"""
How decorator works:

Similar to adding a line(old way of using decorators):
divide = greater_first(divide)
"""

"""
Adding a logger.
"""

def log_deco(func):
	def wrap(a, b):
		print("Values", a, b)
		result = func(a, b)
		print("Result", result)
		return result
	return wrap

def greater_first(func):
	def wrap(a, b):
		if a < b:
			a, b = b, a
		return func(b, a)
	return wrap

@log_deco
@greater_first
def divide(a, b):
	return a / b

print(divide(2, 4))

print("----")
print(divide(4, 2))