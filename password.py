import random
lower = "abcdefghigklmnopqrstuvwxyz"
upper = "ABCDEFGHIGKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,_-"
hello
all = lower+upper+numbers+symbols

length = 16
password = "".join(random.sample(all, length))
print(password)
