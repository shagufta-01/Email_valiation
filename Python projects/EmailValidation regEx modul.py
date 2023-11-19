#a-z,0-9,._==1,@ 1 times,. ka position piche se 2nd last or 3rd last main hona chahiye
import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input('enter your email : ')
if(re.search(email_condition,user_email)):
    print("Right Email")
else:
    print("Wrong Email")