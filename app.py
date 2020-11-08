import mariadb
import dbcreds

while True:
    print ("1. Login")
    print ("2. Sign Up")
    print ("3. Exit")
    select = input("Please select your choice.")
    print()
    if select == "1":
        username = input("Please type your username: ")
        password = input("Please type your password: ")
        print()
        if function.login(username, password):
            while True:
                print("1. Enter a new exploit")
                print("2. Read your exploit")
                print("3. Modify your exploit")
                print("4. Read other hacker's exploit")
                print("5. Modify your account")
                print("6. Exit")
                exploit_select = input("Please input your selection.")
                print()
                if exploit_select == "1":
                    print("Please input your content.")
                    content = input()
                    function.post("username, content")
