import hashlib, sqlite3, os, csv

def check_db1():
    if os.path.exists("admin.db") == True:
        return True
    else:
        return False

def check_db2():
    if os.path.exists("local.db") == True:
        return True
    else:
        return False

def create_db(username, password):
    mydb = sqlite3.connect("admin.db")
    myc = mydb.cursor()
    
    myc.execute("CREATE TABLE password (username text, password text)")
    mydb.commit()
    
    myc.execute("INSERT INTO password VALUES(?,?)", (username, password))
    mydb.commit()
    mydb.close()

def hashing_passwd(passwrd):
    hased_passwrd = hashlib.sha256(passwrd.encode("utf-8")).hexdigest()
    return hased_passwrd

def check_usernm_passwrd(usernm, passwd):
    mydb = sqlite3.connect("admin.db")
    myc = mydb.cursor()
    myc.execute("SELECT * FROM password")
    tup = myc.fetchone()
    c_usernm = tup[0]
    c_passwd = tup[1]

    if usernm == c_usernm and passwd == c_passwd:
        return True
    else:
        return False

def look_db(website):
    mydb = sqlite3.connect("local.db")
    myc = mydb.cursor()
    myc.execute("SELECT * FROM data WHERE website_name LIKE '%"+website+"%'")
    lst = myc.fetchall()
    mydb.commit()
    mydb.close()
    print("\n(Website, Username, Password)")
    print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")
    for i in lst:
        print(i)
        print()

def insert(webnm, usernm, passwd):
    xdb = check_db2()
    if xdb == True:
        pass
    else:
        mydb = sqlite3.connect("local.db")
        myc = mydb.cursor()
        myc.execute("CREATE TABLE data (website_name text, username text, password text)")
        mydb.commit()
        mydb.close()
    mydb = sqlite3.connect("local.db")
    myc = mydb.cursor()
    myc.execute("INSERT INTO data VALUES(?,?,?)", (webnm, usernm, passwd))
    mydb.commit()
    mydb.close()

def update_db(website):
    mydb = sqlite3.connect("local.db")
    myc = mydb.cursor()
    print("""\nWhat To Update
¯¯¯¯¯¯¯¯¯¯¯¯¯¯
1. Username\t\t2. Password\t\t3. Both Username & Password\t\t4. Exit""")
    option = input("$ ")
    if option == "1":
        username = input("Username: ")
        myc.execute("UPDATE data SET username = '"+username+"' WHERE website_name = '"+website+"'")
        mydb.commit()
    elif option == "2":
        passwrd = input("Password: ")
        myc.execute("UPDATE data SET password = '"+passwrd+"' WHERE website_name = '"+website+"'")
        mydb.commit()
    elif option == "3":
        usernm = input("Username: ")
        passwrd = input("Password: ")
        myc.execute("UPDATE data SET username = '"+usernm+"', password = '"+passwrd+"' WHERE website_name = '"+website+"'")
        mydb.commit()

    else:
        print("Invalid Option !")

    mydb.close()

def delete_data(website):
    mydb = sqlite3.connect("local.db")
    myc = mydb.cursor()
    myc.execute("DELETE FROM data WHERE website_name = '"+website+"'")
    mydb.commit()
    mydb.close()

def backup():
    mydb = sqlite3.connect("local.db")
    myc = mydb.cursor()
    myc.execute("SELECT * FROM data")
    lst = myc.fetchall()
    mydb.commit()
    mydb.close()
    
    with open("Password_backup.csv", "w") as f:
        csvwriter = csv.writer(f)
        field = ["Websites", "Username", "Password"]
        main_lst = []
        for i in lst:
            temp_lst = []
            for j in i:
                temp_lst.append(j)
            main_lst.append(temp_lst)
        csvwriter.writerow(field)
        csvwriter.writerows(main_lst)
    dirpath = os.getcwd()+"\Password_backup.csv"
    print("\nBackup file exported Successfully into {}".format(dirpath))
    print("Please copy the backup file to other directory.")

