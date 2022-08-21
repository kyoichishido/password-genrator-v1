import string
import random
import pyperclip

# Characters to use in password
s_letters = string.ascii_lowercase
c_letters = string.ascii_uppercase
numbers = string.digits
special_char = string.punctuation

p_length = 0

# Getting the length of the password and checking if it's valid
def getPassword():
    global p_length

    p_length = input("\033[47m\033[30mEnter the length of your password:\033[m ")

    if(p_length == "exit"):
        exit()

    try:
        p_length = int(p_length)
        if(p_length > 94):
            print("\033[41m\033[30mPassword length must be less than 95\033[m")
            getPassword()
    except ValueError:
        print("\033[41mPlease enter a number. (Type 'exit' to exit)\033[m")
        getPassword()

getPassword()

# print(p_length)
password_superset = []
password_superset.extend(list(s_letters))
password_superset.extend(list(c_letters))
password_superset.extend(list(numbers))
password_superset.extend(list(special_char))

# print(password_superset)
password = "".join(random.sample(password_superset, p_length))  # sample(iterable objects length)

# join function concatinate list
print("\033[47m\033[30mYour secure password is:\033[m \033[32m", password, "\033[m")

if(p_length < 12):
    print("\033[41m\033[30mNOTE: Password length should be at least 12 for better security\033[m")

Question = input("\033[47m\033[30mDo you want to copy the password to clipboard?\033[m (y/n) ")
if Question == ("y") or Question == ("Y") or Question == ("yes") or Question == ("Yes"):
	pyperclip.copy(password)
	print("\033[47m\033[30mOkay, password copied to clipboard. Bye!\033[m")
else:
	print("\033[47m\033[30mOkay, bye!\033[m")