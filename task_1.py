while True:
    option =input("(Enter Marks- Press 1) - (Retrive Marks - Press 2) - ('quit' for exit) : ")
    if option== '1':
        rollno= int(input("Enter your Roll number: "))
        print("Enter your marks in the following subjects: ")
        urdu= int(input("Urdu: "))
        eng= int(input("English: "))
        python= int(input("Pyhton: "))

        marks= {rollno : {'urdu': urdu, 'eng': eng, 'python': python}}

        file = open('marksheet.txt','a')
        file.write(str(marks)+"\n")
        file.close()

    elif option== '2':
        file = open('marksheet.txt','r')
        record = []
        for marks_data in file.readlines():
            marks_data = eval(marks_data)
            record.append(marks_data)
                
        entered_no= int(input("Enter the roll no to retrieve data: "))
        particular_sub = input("Enter the subject to retrieve marks: ") 
        for marks in record:
            if entered_no in marks.keys():
                print("-----------------------------------------------------")
                print("Marks of Roll no",entered_no,": ", marks[entered_no] )
                print("Marks in the particular subject is: ", marks[entered_no][particular_sub])
                print("-----------------------------------------------------")
            file.close()


    elif option== 'quit':
        print("Quit! Thank you")
        break

    else:
        print("Give input in the given constraints")