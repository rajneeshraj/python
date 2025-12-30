a = [1,3,4,5,2,1,3,9,3]
print("the number of times the value 3 appears in the list: ", a.count(3))
a.sort()
print(f"Sort the list and print: {a}")

numbers = {1, 2, 3, 4, 5}
numbers.add(6)
print("add '6' from set ", numbers)

numbers = {1, 2, 3, 4, 5}
numbers.remove(3)
print("remove 3 from set: ", numbers)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3= set1.intersection(set2)
print("intersection of set1 and set2 : ", set3)

fruits = ('apple', 'banana', 'apple', 'cherry')
print("count and print the number of occurrences of the element 'apple : ", fruits.count("apple"))

tuple1 = (1, 2, 3) 
tuple2 = (4, 5, 6)
tuple3=tuple1+tuple2
print("concatenate tuple1 and tuple 2", tuple3)

person = {"name": "Alice", "age": 30, "city": "New York"}
print("print age value: ", person.get("age"))
person.update({"gender":"M"})
print(person)
person.pop("city")
print(person)

dict1 = {"a": 1, "b": 2} 
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(dict1)
