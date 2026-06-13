import time
from datetime import datetime, timedelta

"""
Consider the function:

# def brew_tea():
# 	print("Brewing tea...")
# 	time.sleep(1)
# 	print("Tea is ready!")

We need to get time taken

# def brew_tea():
# 	start_time = time.time()
# 
# 	print("Brewing tea...")
# 	time.sleep(1)
# 	print("Tea is ready!")
# 
# 	end_time = time.time()
# 	print(f"Task time: {end_time - start_time} seconds.")

But this violates Single Responsibility Principle.
It performs two tasks, brewing tea and timing the process.

In programming a function should focus on a single well-defined responsibility,
to make code reusable.
"""

# def timer_dec(base_fn):
# 	def enhance_fn():

# 		start_time = time.time()

# 		base_fn()

# 		end_time = time.time()
# 		print(f"Task time: {end_time - start_time} seconds.")

# 	return enhance_fn


# @timer_dec
# def brew_tea():
# 	print("Brewing tea...")
# 	time.sleep(1)
# 	print("Tea is ready!")

# # brew_tea = timer_dec(brew_tea)
# brew_tea()

"""
Adding decorator is same as adding line:

# brew_tea = timer_dec(brew_tea)
"""


"""
Return optimal time window to drink the tea:
"""

def timer_dec(base_fn):
	def enhance_fn():

		start_time = time.time()

		result = base_fn()

		end_time = time.time()
		print(f"Task time: {end_time - start_time} seconds.")

		return result

	return enhance_fn


@timer_dec
def brew_tea():
	print("Brewing tea...")
	time.sleep(1)
	print("Tea is ready!")
	return f"Drink tea by {datetime.now() + timedelta(minutes=30)}"


print(brew_tea())