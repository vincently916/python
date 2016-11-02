import random
import string
symbols = "~!@#$%^&*()_|<>?=+-"
char = string.uppercase + string.lowercase +  symbols + string.digits
password = " "
counter = 0
while counter <=15:
 temp = random.choice(char)
 password = password + temp 
 counter +=1

print password 
