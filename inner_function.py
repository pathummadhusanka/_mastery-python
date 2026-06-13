"""
# Returning an inner function with brackets
"""

# def outer():
# 	print("From outer function")

# 	def inner():
# 		print("From inner function")

# 	return inner() # inner() get executed

# something = outer()
# print(something)

"""
# Returning an inner function without brackets (Function name)
"""

def outer():
	print("From outer function")

	def inner(argument):
		print("From inner function", f"Argument: {argument}")

	return inner

something = outer()

print("----")
print(something)
print(type(something)) # Returns a function type

print("----")
something("Testing") # inner() function get executed here

print("----")
outer()("Testing") # Same as something()

# You can chain as many () calls as you want,
# 	as long as each call returns another callable