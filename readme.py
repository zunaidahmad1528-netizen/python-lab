# python-lab
# A collection of Python code samples, mini projects, and logic-building exercises.
collection = {1, 2, 3, 4, 5}
print(collection)
print(type(collection))

collection = {}
print(collection)
print(type(collection))
collection = {1,2,3,3.5,33.44, "mohd", True, False, "zunaid"}
print(collection)
print(type(collection))

collection.add(29)
print(collection)
collection.remove(29)
print(collection)

collection.remove("zunaid")
collection.add("rihan")
print(collection)

collection.discard(45)
print(collection)

collection.clear()
print(collection)


col = {1,2,3,4,5,6, (7,8,9)}
# print(col)
# print(type(col))

col.pop()
print(col)

# Set Operations (Mathsematical Operations)
a = {1,2,3,4,5,5,5}
b = {4,5,6,7,8,8}
print(a.union(b))
print(a | b)

print(a.intersection(b))
print(a & b)
 
print(a.difference(b))
print(a - b)

print(b.difference(a))

print(a ^ b)
print(a.symmetric_difference(b))

print(b ^ a)

#  practice question



dict = {
    "table" : ("a piece of furniture" , "list of facts & figurea"),
    "cat" : "a small animal"
}
print(dict)
print(type(dict))

set = {"py", "ja", "c++", "py", "js", "ja", "py", "ja", "c++", "c"}
print(set)
print(len(set))


dictionary = {}
print(dictionary)
English = int(input("Enter your english marks :"))
dictionary.update({"English" : English})
Math = int(input("Enter your math marks :"))
dictionary.update({"Math" : Math})
Scieence = int(input("Enter your science marks :"))
dictionary.update({"Science" : Scieence})
print(dictionary)


set = {"9",9.0}
print(set)

set = {
    ("int" , 9),
    ("float" , 9.0)
}
print(set)