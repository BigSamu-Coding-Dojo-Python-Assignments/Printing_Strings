# STRING LITERALS

print("this is a sample string")

x = "Hello Python"
print(x)
y = 42
print(y)

# STRING CONCATENATION

name = "Zen"
print("My name is", name)
name = "Zen"
print("My name is " + name)

# STRING INTERPOLATION

# F-Strings (Literal String Interpolation)

first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")

# string.format() -> method prior to F-String method

first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.

# string.format() -> and even older method for interpolation

hw = "Hello %s" % "world" 	# with literal values
py = "I love Python %d" % 3 
print(hw, py)
# output: Hello world I love Python 3
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27

# BUILT_IN STRING METHODS

x = "hello world"