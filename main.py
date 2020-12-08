import string
import random


s_letters = string.ascii_lowercase
c_letters = string.ascii_uppercase
numbers = string.digits
special_char = string.punctuation
p_length = int(input("enter length of your password "))
# print(p_length)
password_superset = []
password_superset.extend(list(s_letters))
password_superset.extend(list(c_letters))
password_superset.extend(list(numbers))
password_superset.extend(list(special_char))
# print(password_superset)
password = "".join(random.sample(password_superset, p_length))  # sample(iterable objects length)
# join function concatinate list
print("your secure password is ", password)