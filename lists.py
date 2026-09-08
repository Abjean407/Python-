#PRacticing lists.  Also practicing methods like title and upper to choose a specific listed item in a variable.

bikes =['mongoose', 'huffy', 'diamondback']
print(bikes[0].title())
print(bikes[1].title())
print(bikes[2].upper())
print(bikes[-1])                              #-1 is the syntax to access the last item on a list.
print(bikes[-2].removeprefix('hu').upper())   #-2 returns the second from the end of the list and so on. 


#Practicing pulling a specific value from a variable list and creating a script

message = f"My first bike was a {bikes[0].title()}, I loved that bike so much."
print(message)

print()
print('-Names-')
#quick exercise from Python Crash Course
names = ['Greg', 'timothy', 'samuel']
print(names[0])
print(names[1])
print(names[2])

print()
#greeting Exercise
message_1 = 'It is so nice to see you '
print(f'{message_1}{names[0]}')
print(f'{message_1}{names[1].title()}')
print(f'{message_1}{names[2].title()}')

#Statement Exercise with lists
print()
print('-Cars-')
cars = ['Audi','Honda','BMW']
print(cars[0])
print(cars[1])
print(cars[2])
print(f"One day I would love to own a {cars[0]}!")
print(f"I've heard {cars[2]}'s are not so reliable")
print(f"Out of all of the cars in this list {cars[1]}'s are the most fuel efficient and long lasting cars")

print()
print('-adding elements-')
#Practicing changing the value in a list
motorcycles = ['Honda', 'Ducati', 'Indian']
motorcycles[0] = 'Harley'
print(motorcycles)

#appending a variable to a list
cycles = ['Tricycle', 'Bicycle',]
cycles.append('unicycle')
print(cycles)

#inserting elements to a list
cycles.insert(1,'Dragon')
print(cycles)

#deleting element from a list
del cycles[0]
print(cycles)

#using the Pop method
popped_cycles = cycles.pop()
print(cycles)
print(popped_cycles)


#More practice with .pop,,, guest scenario 
print()
print('-guests-')
guest_names = ['Anthony','Brian','Kody']

cancelled_guest = guest_names.pop(1)
print(f"I'm sorry but {cancelled_guest} said he would not be able to it make it today.")

#Practice with the .remove method
print()
print('-Consoles-')
consoles = ['Ps5', 'Xbox','Gamecube']
consoles.remove('Ps5')
print(consoles)
print()
#guest list Exercise
print('-Guest Exercise-')
guest_list = ['Michael Jackson','Ricky Bobby','Roberto Clemente']
print(f"Hey {guest_list[0]} do you want to come to my dinner party this saturday!?")
print(f"Hey {guest_list[1]} do you want to come to my dinner party this saturday!?")
print(f"Hey {guest_list[2]} do you want to come to my dinner party this saturday!?")
print()
print(f"{guest_list[1]} can not make it to the dinner party this saturday")

guest_list[1]= 'Jesus'
print()

print(f"Hey {guest_list[0]} do you want to come to my dinner party this saturday!?")
print(f"Hey {guest_list[1]} do you want to come to my dinner party this saturday!?")
print(f"Hey {guest_list[2]} do you want to come to my dinner party this saturday!?")
print()
guest_list.insert(0,'Eugene')
guest_list.insert(2,'Kevin')
guest_list.append('Timothy')
print(guest_list)
print(f"Hey {guest_list[0]} do you want to come to my dinner party this saturday!?")
print(f"Hey {guest_list[1]} do you want to come to my dinner party this saturday!?")
print(f"Hey {guest_list[2]} do you want to come to my dinner party this saturday!?")
print(f"Hey {guest_list[3]} do you want to come to my dinner party this saturday!?")
print(f"Hey {guest_list[4]} do you want to come to my dinner party this saturday!?")
print(f"Hey {guest_list[5]} do you want to come to my dinner party this saturday!?")
print("Guys I also found a bigger table for all of us to sit at")
print()
print("Sorry I can only invite two guests to this dinner party")

popped_guests = guest_list.pop()
print(f"im sorry i had to uninvite you {popped_guests}")
print()
popped_guests = guest_list.pop()
print(f"im sorry i had to uninvite you {popped_guests}")
print()
popped_guests = guest_list.pop()
print(f"im sorry i had to uninvite you {popped_guests}")
print()
popped_guests = guest_list.pop()
print(f"im sorry i had to uninvite you {popped_guests}")
print()
print(f"Hey you're still invited to the dinner, see you soon! {guest_list[0]}")
print(f"Hey you're still invited to the dinner, see you soon! {guest_list[1]}")

del guest_list[0]
del guest_list[0]
print(guest_list)

#organizing a list

toys=['batman', 'superman','deadpool']
print(toys)
toys.sort()
print(toys)
print()
toys.reverse()
print(toys)
print(len(toys))


