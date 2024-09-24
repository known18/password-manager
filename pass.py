from random import choice
def passgen():
 l=['q','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b',
   'n','m','1','2','3','4','5','6','7','8','9','0']
 long=int(input("enter the length of password: "))
 if long<=1:
   print("password length is too short")
 else:
   long=long-1
   passw1=choice(l)
   t=1 
   while t<=long:
       passw2=choice(l)
       passw1=passw1+passw2
       t+=1
   print(passw1)
#password manager 
def passkeeper():
  logid=input("enter the login ID:")
  logpass=input("enter the login password:") 
  f= open("Password.txt","a")
  f.write(logid+"|"+logpass+"\n")
def passreader():
  with open("Password.txt","r") as f:
   for line in f:
    userid,password= line.strip().split("|")
    print("logid:",userid,",","password:",password)
while True:
   print(" enter 1 to create a password \n",
         "enter 2 to save a password \n",
         "enter 3 to view password \n",
         "enter 4 to exit")
   cho=int(input("enter your choice: "))
   if cho==1:
      passgen()
   elif cho==2:
     passkeeper()
   elif cho==3:
      passreader()
   elif cho==4:
      break 
   else:
     print("Invalid choice")
   

       
    
