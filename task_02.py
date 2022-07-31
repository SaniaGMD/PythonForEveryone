Q#6 (10) 
We have a set of strings {"hasan", "ahmad", "bilal", "goreyo", "tokeyo", "multan", "fatima", "yasmin"}.
We want to group such strings into a separate list and show that have equal number of characters in them.
Also we want to show the number of similar length strings on the screen with their length.
Example output may look like this:
3 strings of length 9 are found
The strings are: 
[ a list of such strings ]



data= {"hasan", "ahmad", "bilal", "goreyo", "tokeyo", "multan", "fatima", "yasmin"}
str_len3=[]
str_len4=[]
str_len5=[]
3str_len6=[]
str_len7=[]

for i in data:
    if len(i)== 3:
        str_len3.append(i)
    elif len(i)==4:
        str_len4.append(i)
    elif len(i)==5:
        str_len5.append(i)
    elif len(i)==6:
        str_len6.append(i)
    elif len(i)==7:
        str_len7.append(i)
    else:
        pass
print("Length of strings having 4 charaters is: ", len(str_len4), str_len4) 
print("Length of strings having 5 charaters is: ", len(str_len5), str_len5) 
print("Length of strings having 6 charaters is: ", len(str_len6), str_len6) 
print("Length of strings having 7 charaters is: ", len(str_len7), str_len7) 

