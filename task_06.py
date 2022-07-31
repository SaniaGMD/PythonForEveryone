
We have a string "I am studying hard to learn AI and BD" and we want to make a new string from this one.
The new string should look like "studying learn and"


#method 1 : by slicing
s = "I am studying hard to learn AI and BD"
new_s= s[5:13] +" " + s[22:27] +" " + s[31:34] 
print("The new string is:", new_s)


#method 2
def Convert(string):
    li = list(string.split(" "))
    return li

s = "I am studying hard to learn AI and BD"
list_s= Convert(s)
new_string= list_s[2]+ " " + list_s[5]+ " "+ list_s[7]
print("The new string is:", new_string)