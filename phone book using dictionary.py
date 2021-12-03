main={}
while 1:
    print(" 1: Insert \n 2: View \n 3: Update \n 4: Delete")
    option=int(input(" Enter your option :"))
    a={}
    if option==1:
        name=input(" Enter your name : ")
        email=input(" Enter your EMail ID :")
        phno=int(input(" Enter your Mobile Number :"))
        a={"name":name,"email":email,"phone number":phno}
        main[name]=a
    elif option==2:
        name=input(" Enter your Name :")
        if name in main:
            print(main[name])
        else:
            print(" Name not Found ... Try Again...")

    elif option==3:
        name=input("Enter your Name to be updated :")
        print(" Edit option :- \n 1: name \n 2: email \n 3: phone number")
        b= int(input(" Choice : "))
        if b==1:
            new_name=input(" Enter a New name :  ")
            main[name].update({"name":new_name})
            main[new_name]=main[name]
            del main[name]
            print(main)
        # if name2 in main:
        #     main[name].update()=input(" Enter your name")
        #     main[email].update()=input(" Enter your EMail ID :")
        #     main[phone_no].update()=int(input(" Enter your Mobile Number :"))
        elif b==2:
            new_email=input("Enter a new Email ID : ")
            a.update({"email":new_email})
            a=main[name]
            print (a)
        elif b==3:
            new_phno = int(input("Enter a new phone number : "))
            a.update({"phone number":new_phno})
            print(a)
        else:
            pass
    elif option==4:
        name=input(" Enter a name to delete : ")
        if name in main:
            del main[name]
            print(name,' deleted')
        else:
            print(" Not available")
    else:
        break