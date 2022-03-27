
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

print(friends)
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])

print("The last element is: "+ friends[-1])
print("The list starting from element 1 is: " + str(friends[1:]))
print("The list range from 1 to 3 is: " + str(friends[1:3])) # up to but not including 3

friends[1] = "Mike"
print("Element 1 has been changed to: " + friends[1])
