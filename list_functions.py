lucky_numbers = [42, 8, 15, 16, 23, 25]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

print("\nfriends list: " + str(friends))
print("lucky_numbers list: " + str(lucky_numbers))

friends.sort()
lucky_numbers.sort()
print("\nsort: " + str(friends))
print("sort: " + str(lucky_numbers))

friends.reverse()
lucky_numbers.reverse()
print("\nreverse: " + str(friends))
print("reverse: " + str(lucky_numbers))

friends2 = friends.copy()
print("\ncopy: " + str(friends2))

friends.append("Paul") # Add element onto end of list
print("\nappend: " + str(friends))
print("Index position for \"Paul\": " + str(friends.index("Paul")))
print("Count for \"Jim\": " + str(friends.count("Jim")))
friends.insert(1,"Kelly") #Add element at index position 1
print("insert: " + str(friends))
friends.pop() # remove (pop) last element off the list
print("pop: " + str(friends))
friends.remove("Jim")
print("remove: " + str(friends))

friends.extend(lucky_numbers) # Add lucky_numbers[] to end of list
print("\nextend: " +str(friends))
friends.clear() # remove all elements
print("clear: " +  str(friends))


