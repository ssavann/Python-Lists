#Make a lists in Python
statesOfAmerica = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", 
"Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", 
"Virginia", "New York" ]


#to call the list with a [] "bracket"
print(statesOfAmerica[4])
print(statesOfAmerica[0])
print(statesOfAmerica[10])
print(statesOfAmerica[-2])  #from end of list to left


#to add more item in your list, you "append"
print("======== append ===========")
statesOfAmerica.append("North Carolina")
statesOfAmerica.append("Rhode Island")
statesOfAmerica.append("Vermont")

print(statesOfAmerica)


print("======== extend ===========")
statesOfAmerica.extend(["Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana"])

print(statesOfAmerica)


print("======== Length ===========")

num_of_states =  len(statesOfAmerica)   #will count how many elements in the list

print(statesOfAmerica[num_of_states - 1])     #will print the last element of the list
#need to add "-1" otherwise it will be out of range