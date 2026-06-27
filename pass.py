correctpass="1234"
for i in range(1,6):
 pass1=input("enter pass")
 if (correctpass==pass1):
  print("logged sucessfully")
 else:
    print("wrong pass")
    break
 
 #age
 age = int(input("enter your age"))
if (age<=13):
 print("child")
 elif (13<age<18):
  print("teenager")
 elif (20<age< 60):
  print("adult")
elif (age>60):
 print("senior citizen")
        break
 