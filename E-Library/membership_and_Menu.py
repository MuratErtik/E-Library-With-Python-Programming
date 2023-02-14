import random


import time


import sqlite3


import lib



class Membership():
    def __init__(self):

        self.Create_Connection()

    def Create_Connection(self):
        self.connection = sqlite3.connect("Members.db")
        self.cursor = self.connection.cursor()
        query = "CREATE TABLE IF NOT EXISTS Members (Username TEXT,Password TEXT,Email TEXT,Recovery_Code INT)"
        self.cursor.execute(query)
        self.connection.commit()


    def Finish_Connection(self):
        self.connection.close()




    def Create_Account(self, user_name, password, email):
        query = "INSERT INTO Members VALUES (?,?,?,?)"
        recovery_cod = random.randint(1000, 9999)
        self.cursor.execute(query, (user_name, password, email, recovery_cod))
        self.connection.commit()





    def Login_Account(self,username,password):
        query = "SELECT * FROM Members WHERE Username = ? and Password = ?"
        self.cursor.execute(query, (username,password))
        list1 = self.cursor.fetchall()


        if len(list1) == 0 :
            print("There is no such account!")

        else:
            if username == list1[0][0] and password == list1[0][1]:
                print("Checking in.....")
                time.sleep(3)
                print("Application is opening please wait...")
                time.sleep(3)
                print("""

                        ************************************************
                             WELCOME TO LIBRARY APPLICATİON            * 
                                                                       *
                        OPTIONS:                                       * 
                                                                       * 
                        1.) Show the all  books                        * 
                                                                       * 
                        2.) Query to book                              * 
                                                                       * 
                        3.) Add the book                               * 
                                                                       * 
                        4.) Delete the book                            * 
                                                                       * 
                        5.) Update the edition                         * 
                                                                       *      
                        6.) Settings of account                        *         
                                                                       * 
                                                                       * 
                        press 'q' for exit                             * 
                                                                       * 
                        ************************************************
                        """)


                while True:
                    action = input("Select your action you want to do in App: ")
                    if action == "q":
                        print("The Application is closing...")
                        time.sleep(4)
                        print("the Application is closed....")
                        break

                    elif action == "1":
                        book = lib.Library()
                        print("*************All the Books**************")
                        time.sleep(3)
                        book.Show_ALL_Books()


                    elif action =="2":
                        book1 = lib.Library()
                        book2 = input("Please enter which book  you  want:  ")
                        print("Please waiting.....")
                        time.sleep(3)
                        book1.Query_To_Book(book2)


                    elif action == "3":

                        book3 = lib.Library()

                        print("Enter the information of the book you want to add to the library.")
                        time.sleep(1)
                        book4 = input("Please enter the book name:")
                        writer = input("Please enter the writer:")
                        publisher = input("Please enter the publisher:")
                        type = input("Please enter the type:")
                        number_of_page = input("Please enter the number of page:")
                        edition = input("Please enter the edition:")

                        print("Adding.....")
                        time.sleep(2)
                        book3.Add_To_Book(book4,writer,publisher,type,number_of_page,edition)
                        print("The book has been added your library")

                    elif action == "4":

                        book5 = lib.Library()
                        book6 = input("Which book do you want to the delete? Please Enter:")

                        print("being deleted...")
                        book5.Delete_Book(book6)


                    elif action == "5":
                        book7 = lib.Library()
                        book8 = input("Which book do you want to update the edition? Please Enter:")
                        print("Updating...")
                        time.sleep(3)
                        book7.Update_Edition(book8)



                    elif action == "6":
                        print("""
                        ************************************************
                        
                            Menu Settings:
                            
                            1.) Delete Account 
                            
                            2.) Change Username
                        
                            3.) Change Password
                        
                            press 'q' for exit
                            
                        *************************************************    
                            
                            
                        """)
                        while True:
                            action = input("Select your action you want to do in settings: ")
                            if action == "q":
                                print("The Application is closing...")
                                time.sleep(4)
                                print("the Application is closed....")
                                break

                            elif action == "1":
                                member = Membership()

                                name = input("enter your username:")
                                email = input("enter your email:")

                                member.Delete_Account(name,email)

                            elif action == "2":
                                member1 = Membership()

                                name1 = input("please enter your username:")
                                new_name = input("Please enter your new username:")

                                member1.Change_Username(name1,new_name)


                            elif action == "3":
                                member2 = Membership()

                                name2 = input("please enter your username:")
                                password1 = input("please enter your password:")
                                password2 = input("please enter your password:")

                                member2.Change_Password(name2,password1,password2)



                            else:
                                print("You select invalid action! Please enter correct action")



                    else:
                        print("You select invalid action! Please enter correct action")





    def Delete_Account(self,name,email):
        query = "SELECT * FROM Members WHERE Username = ? and Email = ?"
        self.cursor.execute(query, (name, email))
        list1 = self.cursor.fetchall()

        if len(list1)== 0:
            print("There is no such account!")

        else:
            sure = input("Are you sure? (Y or N) ")
            if sure ==  "N":
                print("Loading...")
                time.sleep(2)
                print("Canceled")
            elif sure == "Y":
                query2 = "DELETE FROM Members WHERE Username =?"
                self.cursor.execute(query2,(name,))
                self.connection.commit()
                print("Loading...")
                time.sleep(2)
                print("Deleted")




    def Change_Username(self,name,new_name):
        query = "SELECT * FROM Members WHERE Username = ? "
        self.cursor.execute(query, (name,))
        list1 = self.cursor.fetchall()

        if len(list1) == 0:
            print("There is no such account!")

        else:
            sure = input("Are you sure: (Y or N)")
            if sure == "N":
                print("Loading...")
                time.sleep(2)
                print("Canceled")
            elif sure == "Y":
                query2 = "UPDATE   Members SET Username = ? WHERE Username =?"
                self.cursor.execute(query2,(new_name,name))
                self.connection.commit()
                print("Loading...")
                time.sleep(2)
                print("Changed")




    def Change_Password(self,name,password,new_password):
        pass

        query = "SELECT * FROM Members WHERE Username = ? AND Password=?"
        self.cursor.execute(query, (name,password))
        list1 = self.cursor.fetchall()

        if len(list1) == 0:
            print("There is no such account!")

        else:
            sure = input("Are you sure: (Y or N)")
            if sure == "N":
                print("Loading...")
                time.sleep(2)
                print("Canceled")
            elif sure == "Y":
                query2 = "UPDATE   Members SET Password = ? WHERE Username =?"
                self.cursor.execute(query2, (new_password, name))
                self.connection.commit()
                print("Loading...")
                time.sleep(2)
                print("Changed")



    def Recovery_Code(self,username,email):
        query = "SELECT * FROM Members WHERE Username = ? and Email =?"
        self.cursor.execute(query, (username, email))
        list1 = self.cursor.fetchall()

        if len(list1) == 0 :
            print("No found any data!")
        else:
            if email == list1[0][2] and username == list1[0][0]:

                recovery_code = int(input("enter your recovery code:"))
                if recovery_code == list1[0][3]:
                    print("loading.....")
                    time.sleep(4)
                    print("your password is:", list1[0][1])
                else:
                    print("your recovery code is false try later!")

            else:
                print("loading...")
                time.sleep(4)
                print("your email or username are false try later")