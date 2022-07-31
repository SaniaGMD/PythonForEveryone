
Here is a list of names: ['Abdullah', 'Tayyaba', 'Waheed', 'Fatima', 'Basim', 'Hira']
Write a program that goes over this list and separates the names of males and females in two different lists and 
after getting done with them, shows the lists on screen.
Hint: There is a pattern to these names. Find the pattern and use % operator







data = ['Abdullah', 'Tayyaba', 'Waheed', 'Fatima', 'Basim', 'Hira'] 
female= []
male= []
for i in range(len(data)):
    if i%2==0:
        male.append(data[i])
    else:
        female.append(data[i])

print("Male data_list: ", male )
print("Female data_list: ", female )