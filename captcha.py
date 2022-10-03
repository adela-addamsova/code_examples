"""
Program generates captcha code which is used to verify if user is not a robot.
User is about to transcribe the generated code.
Code is combination of randomly generated 5 signs of upper and lower alphabet signs and 0-9 numbers.
"""
import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
digits = "0123456789"

captcha = ""
transcribe = ""

for i in range(0, 5):
    x = random.randint(1, 3)
    if x == 1:
        captcha += random.choice(lower)
    if x == 2:
        captcha += random.choice(upper)
    if x == 3:
        captcha += random.choice(digits)

print(captcha)

transcribe = input("Write the captcha code: ")

if transcribe == captcha:
    print("Code was written correctly.")
else:
    while transcribe != captcha:
        transcribe = input("Write the captcha code: ")