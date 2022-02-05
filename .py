name = input("Enter a name:")
MyNamesContainer = {
"Maria" : 23,
"Anna" : 19,
"Jack" : 5,
"Alex" : 12,
"John" : 18}
if name in MyNamesContainer:
	print("Found it! It is corresponds to", 
		MyNamesContainer[name])
else: print("No such name in the container.")
