tup = (2,3,4,5,6,8,7,9,2,2,5,6,)
print(tup)

print(tup[0])
print(tup[1])

tup =(1.0,)
print(tup)
print(type(tup))tup  =


tup = (1,2,3,4,5,6,7,8,9)
print(tup[1:4])

tup = (1,2,3,4,5,6,7,8,9)
print(tup.index(3))

tup = (1,2,3,4,5,6,7,8,9)
print(tup.count(3))


question 

list = input("enter your favurite 3 movies name :")

list2 = [list]
print(list2)
movies = []
movi1 = input("enter your first movie name :")
movi2 = input("enter your second movie name :")
movi3 = input("enter your third movie name :")
movies.append(movi1)
movies.append(movi2)
movies.append(movi3)
print(movies)

list = [1, 2, 3, 2, 1]
list.copy()
print(list)
list.reverse()
print(list)

list1 = int(input("enter your list :"))

copy_list = list1.copy()
copy_list.reverse()

if (copy_list == list):
    print("palindrome")
else:
    print("not palindrome")

grade = ["c", "D", "A", "A", "B", "B", "A"]
grade.count("A")
print(grade.count("A"))
list = []
list.append(grade.count("A"))
print(list)

grade.sort()
print(grade)