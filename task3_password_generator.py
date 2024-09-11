import random
letters_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
              'v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
              'Q','R','S','T','U','V','W','X','Y','Z']
numbers_list=['1','2','3','4','5','6','7','8','9','0']
symbols_list=['`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','{','}','[',']','|',
              ';',':',',','<','.','>','/','?']
print("Welcome to password generator!!")
letters=int(input("How many letters you want in your password??"))
numbers=int(input("How many numbers you want in your password??"))
symbols=int(input("How many symbols you want in your password??"))
password_list=[]
for i in range(1,letters+1):
    char=random.choice(letters_list)
    password_list+=char
for i in range(1,numbers+1):
    num=random.choice(numbers_list)
    password_list+=num
for i in range(1,symbols+1):
    sym=random.choice(symbols_list)
    password_list+=sym
random.shuffle(password_list)
password=""
for i in password_list:
    password+=i
print('Your password is:\n',password)