A recruitment activity is taking place at a company. The physical requirements include weight between 50kg and 100kg, 
BMI more than 10 but less than 20, and height more than 5 feet.
The company needs a software solution to automate the selection process. When user enters details, the software responds 
with either "selected" or "not selected".
Company wants to select those who fulfill the above mentioned criteria but if someone with weight exceeding the limit, 
or BMI exceeding the mentioned limit applies and the person is married, he/she gets selected. Similarly if height is less
than the requirement and the applicant is married, he/she gets selected.







print("*********Enter your Details please*********")
weight= float(input("Your Weight: "))
BMI= float(input("Your BMI: "))
height= float(input("Your Height: "))
marrital_status = input("Married(Press 1), Unmarried (Press 0) : ")

if (weight>50 and weight<100) and (BMI>10 and BMI<20) and (height>5):
    print("            ---------------------------             ")
    print("         Congratulations, you're Selected")
    print("            ---------------------------             ")
elif marrital_status == '1':
    if (weight>50 and weight<100) or (BMI>10 and BMI<20) or (height<=5 or height >=5):
        print("            ---------------------------             ")
        print("         Congratulations, you're Selected")
        print("            ---------------------------             ")
else:
    print("            ---------------------------             ")
    print("           Sorry, you're not eligible")
    print("            ---------------------------             ")