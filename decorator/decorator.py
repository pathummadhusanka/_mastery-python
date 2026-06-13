"""
# Decorator
# 	A function that extends the behavior of another function without modifying the base function.
"""


"""
Add sprinkles to ice cream using decorator:
"""

# def add_sprinkles(func):
# 	def wrapper():
# 		print("You add sprinkles")
# 		func()
# 	return wrapper

# @add_sprinkles
# def get_ice_cream(): # Base function
# 	print("Here is your ice cream")

# get_ice_cream()

"""
Wrapper is necessary.
Otherwise decorator will execute the add_sprinkles() even without get_ice_cream() statement.
"""

# def add_sprinkles(func):
# 	print("You add sprinkles")
# 	func()

# @add_sprinkles
# def get_ice_cream():
# 	print("Here is your ice cream")

"""
Can add multiple decorators.
"""

# def add_sprinkles(func):
# 	def wrapper():
# 		print("You add sprinkles")
# 		func()
# 	return wrapper

# def add_fudge(func):
# 	def wrapper():
# 		print("You add fudge")
# 		func()
# 	return wrapper

# @add_sprinkles
# @add_fudge
# def get_ice_cream():
# 	print("Here is your ice cream")

# get_ice_cream()

"""
Passing arguments to base function.
Need to setup *args and **kwargs
"""

def add_sprinkles(func):
	def wrapper(*args, **kwargs):
		print("You add sprinkles")
		func(*args, **kwargs)
	return wrapper

def add_fudge(func):
	def wrapper(*args, **kwargs):
		print("You add fudge")
		func(*args, **kwargs)
	return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
	print(f"Here is your {flavor} ice cream")

get_ice_cream("vanilla")