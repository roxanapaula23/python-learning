#Adds an element at the end of the list
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)

#Removes all the elements from the list
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()

#Returns a copy of the list
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()

#Returns the number of elements with the specified value
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)

#Add the elements of a list (or any iterable), to the end of the current list
fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)	

#Returns the index of the first element with the specified value
fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)	

#Adds an element at the specified position
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")

#Removes the element at the specified position
fruits = ['apple', 'banana', 'cherry']
x = fruits.pop(1)

#Removes the item with the specified value	
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")

#Reverses the order of the list
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()

#Sorts the list
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)

