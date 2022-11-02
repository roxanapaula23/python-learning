x = "dynamically-typed"
def myfunc():
  print("Python is " + x)
myfunc()

x = "dynamically-typed"
def myfunc():
  x = "a high-level language"
  print("Python is " + x)
myfunc()
print("Python is " + x)

def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

x = "awesome"
def myfunc():
  global x
  x = "a general-purpose language"
myfunc()
print("Python is " + x)