import pwinput 
database = {"ujjwallamsal": "ujjwal12345", "nepal": "nepal123",'admin':"coursely@123"}
username = input("Enter Your Username : ")
for i in database.keys():
    if username == i:
        password = pwinput.pwinput("Enter Your Password : ")
        if password == database[i]:
            print("You are logged in")
            break
        else:
            print("Incorrect Password")
            break
    else:
        continue
else:
    print("Username Not Found")
