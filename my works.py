main={}
while 1:
    print(" 1: insert \n 2: view \n 3: update \n 4: delete")
    option = int(input(" Enter your option : "))
    a={}
    if option==1:
        name=input(" Enter your name : ")
        email=input(" Enter your EMail ID :")
        ph_no=int(input(" Enter your Phone Number :"))
        a["name"]=name
        a["email"]=email
        a["mobile Number"]=ph_no
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
        elif b==2:
            new_email=input("Enter a new Email ID : ")
            main[name].update({"email":new_email})
            main[new_email]=main[name]
            print (main)
        elif b==3:
            new_phno = int(input("Enter a new phone number : "))
            main[name].update({"phone number":new_phno})
            main[new_phno]=main[name]
            print(main)
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