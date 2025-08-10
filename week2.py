my_list = []
#add 10, 20,30,40
my_list.append( 10 )
my_list.append( 20 )
my_list.append( 30 )
my_list.append( 40 )
#insert 15 in second position
my_list.insert(1, 15)
#Extend my_list with another list: [50, 60, 70].
my_list.append( 50 )
my_list.append( 60 )
my_list.append( 70 )
#Remove the last element from my_list.
del my_list[7]
#Sort my_list in ascending order.
Ade = sorted(my_list)
#Find and print the index of the value 30 in my_list.
index = my_list.index(30)

print(Ade)