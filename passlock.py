import sys
from main_function import *
print("""
WELCOME TO PASSLOCK
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
""")
xdb = check_db1()
if xdb == True:
    pass
else:
    print("\nPlease setup login credentials for security !")
    username = input("Username: ")
    passwrd = hashing_passwd(input("Password: "))
    create_db(username, passwrd)
    print("Credentials saved successfully !")
    print("PRECAUTIONS: Please Don't Forget Your Credentials !")

print("\nPlease Login")
print("¯¯¯¯¯¯¯¯¯¯¯¯")
usernm = input("Enter Username: ")
passwd = hashing_passwd(input("Enter Password: "))
lresult = check_usernm_passwrd(usernm, passwd)
if lresult == True:
    print('Logged In Successfully !')
    pass
elif lresult == False:
    print("Incorrect Username OR Password !")
    exit()

print("""\nChoose The Options
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
1. Check Data\t\t2. Insert Data
3. Update Data\t\t4. Delete Data
5. Backup\t\t6. Exit""")

condition = True
while condition == True:
    opt = input("\n"+usernm+"|@ ")

    if opt == "1":
        try:
            web = input("\nWebsite Name: ").lower()
            look_db(web)
        except:
            print('No Such Data Inserted !')
    
    elif opt == "2":
        n = int(input("\nEnter the number of website to insert: "))
        if n > 0:
            while n > 0:
                website = input("Name of Website: ").lower()
                username = input("Username: ")
                passwrd = input("Password: ")
                insert(website, username, passwrd)
                n -= 1
        else:
            pass

    elif opt == "3":
        try:
            web = input("\nName of the Website whose credentials to be updated: ").lower()
            update_db(web)
        except:
            print("No Such Data Inserted !")

    elif opt == "4":
        try:
            print("""\n
NOTE: Please cross-check the name of the website.
¯¯¯¯¯ The data will be permanently deleted.""")
        
            web = input("Website: ").lower()
            delete_data(web)
        except:
            print("No Such Data Inserted !")

    elif opt == "5":
        try:
            backup()
        except:
            print("No Data Inserted To Create Backup !")

    elif opt == "6":
        condition = False

    else:
        print("Invalid Choice !")
    
