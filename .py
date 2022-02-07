credits= ('''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			 ~~~~~~~~~~~~Created by~~~~~~~~~~~~~~
			 ~~~~~~~~~~~~SpyroHB_dev~~~~~~~~~~~~~
			 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
			 
####################################################################################################################
print(credits.upper())

name = input("Enter a name:")

MySiblingsContainer = {

"Emy" : 30,

"Mohammed" : 27,

"Mehdi" : 23,

"Younes" : 19,

"Abd raouf" : 10}

shit = 0

while True:

	if name in MySiblingsContainer:

		print("Found it! It is corresponds to",MySiblingsContainer[name])

		break

	if name not in MySiblingsContainer:

			print("No such name in the container.")

	name = input("Enter a name:")

