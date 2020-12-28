#nested lists: a list inside a list

row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]


map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")     #try: 22, 12, 23, 33

horizontal = int(position[0])
vertical = int(position[1])

#selected_row = map[vertical - 1]        #to avoid being out of range add '-1'
#selected_row[horizontal - 1] = "X"

map[vertical - 1][horizontal - 1] = "X"    #will work as well


print(f"{row1}\n{row2}\n{row3}")