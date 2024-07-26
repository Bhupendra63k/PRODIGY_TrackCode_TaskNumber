import re

print()
password=input("enter your password :")
password_length=len(password)
if password_length<8:
    print("please ensure your password has 8 letter")
elif not re.search('[A-Z]',password):
          print("please use atleast a uppercase letter")
elif not re.search('[a-z]',password):
        print("please use atleast a lowercase letter")
elif not re.search('[0-9]',password):
        print("please use atleast a number")
else :
    print("your password is strong")