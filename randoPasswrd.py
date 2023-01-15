import random
import pyperclip

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
sym = "[]{}()*;/,._-"

all = lower + upper + numbers + sym
print ("How long would you like your password?")
len = int(input())
while (len <= 0):
    print("Please enter a positive value")
    len = int(input())
pyperclip.copy("".join(random.sample(all,len)))
password = pyperclip.paste()

print (password)
