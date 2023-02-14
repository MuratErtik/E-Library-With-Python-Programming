import time

import membership_and_Menu

print("""
***************************************************** 
                                                    *
      WELCOME TO THE LIBRARY APPLICATION LOGIN      *
                                                    *
1.) Login your account                              *    
                                                    *
2.) Create a new account                            *
                                                    *
3.) Forget my password                              *
                                                    *
                                                    *
    press 'q' for exit                              *    
                                                    *
                                                    *
*****************************************************
""")





while True:
    action = input("Select your action you want to do: ")
    if action == "q":
        print("The Application is closing...")
        time.sleep(4)
        print("the Application is closed....")
        break


    elif action == "1":
        username = input("please enter your username:")
        password = input("please enter your password:")
        member1 = membership_and_Menu.Membership()
        member1.Login_Account(username,password)



    elif action == "2":
        print("Welcome new member! Please enter your informations")
        time.sleep(3)
        username1 = input("Enter your username:")
        password1 = input("Enter your password:")
        email1 = input("Enter your email:")
        member1 = membership_and_Menu.Membership()
        member1.Create_Account(username1,password1,email1)
        print("Your informations saved successfuly Welcome again")



    elif action == "3":
        username2 = input("Please enter your username:")
        email2 = input("Pleae enter your email:")
        member1 = membership_and_Menu.Membership()
        member1.Recovery_Code(username2,  email2)


    else:
        print("You select invalid action! Please enter correct action")