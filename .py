name = input("Enter a name:")
MyNamesContainer = {
"Maria" : 23,
"Anna" : 19,
"Jack" : 5,
"Alex" : 12,
"John" : 18}
shit = 0
while True:
	if name in list(MyNamesContainer):
		print("Found it! It is corresponds to",MyNamesContainer[name])
		break
	if name not in MyNamesContainer:
			print("No such name in the container.")
	name = input("Enter a name:")
