# Password generator: A tool that generate secure, random passwords based on user defineed criteria like length

import random

characters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
specialchar = ['1','2','3','4','5','6','7','8','9','0','@','#','$','%','&','*','(',')','!','/']

pass_length = int(input("Length of password you want : ")) # password length input
password = ''
while len(password) != pass_length:
    char = random.choice(characters)
    spec = random.choice(specialchar)

    password = password + char
    if len(password)< pass_length:
     password = password + spec

chars = list(password)
random.shuffle(chars)
shuffled = ''.join(chars)
print("Your password is : ",shuffled)
