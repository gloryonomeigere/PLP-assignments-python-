my_list = []                      #creates an empty list
#add values to the list
my_list.append(10)  
my_list.append(20)
my_list.append(30)
my_list.append(40)
print (my_list)

my_list.insert(2, 15)              #inserts a value into the second position in the list
print (my_list)

another_list = [50, 60, 70]        #create a second list
my_list.extend(another_list)       #joins the second list to the first list
print (my_list)

my_list.remove(70)                 #removes the identified value
print (my_list)

my_list.sort()                     #arranges in ascending order, the values in the list 
print (my_list)

print(my_list[3])                  #obtains the value specified by the index position