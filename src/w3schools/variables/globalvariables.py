x = "dynamically-typed"

def my_func():
  print("Python is " + x)
my_func()

def my_func():
  x = "a high-level language"
  print("Python is " + x)
my_func()


print("Python is " + x)

def my_func():
  x = "fantastic"
  print("Inside function: " + "python is " + x)

my_func()


print("outside function: Python is " + x)

x = "awesome"
def my_func():
  global x
  x = "a general-purpose language"
my_func()
print("Python is " + x)