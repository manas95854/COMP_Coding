def login():
    username = input("enter username : ")
    password = input("enter password : ")
    if username == password:
        print("login successfully")
    else:
        print("invalid credentials")

login()