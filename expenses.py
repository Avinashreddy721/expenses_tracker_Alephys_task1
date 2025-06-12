import json

# my json file name is "testfile.json"

with open('testfile.json','r') as files:
    send=json.load(files)
# if you want know your monthly savings from expenditure enter input as "find"
print('if you want know your monthly savings from expenditure enter input as "find"')
print('if u want to want to see the data in json file, enter input as "show"')
user_input=input('enter your required request name : ')
if(user_input =='find'):
    salary=int(input('enter your monthly salary : '))
    expenses=int(input("enter the number of expenses u want to add ex:2/3 : "))
    s=0
    for i in range(0,expenses):
        expenditures=input("enter the expenses such as food ,rent,travels : ")
        if(expenditures =='rent' or expenditures =='food' or expenditures =='travels'):
            r=int(input('enter the amount : '))
            s=s+r
        else:
            print('please enter the valid expenses and try again : ')
            
    print('total monthly saved amount after removing expenditure is : ',salary-s)
    
elif(user_input == "show"):
    l=0
    for k in send:
        l=l+k["Travel"]+k["rent"]+k["Food"]
        print("So monthly savings remained are : ",k["id"],"is",k["salary"]-l)
else:
    print("please enter the valid option and try again : ") 
    