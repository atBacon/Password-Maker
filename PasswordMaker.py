L = 0 #length
N = 0 #numeric characters
X = 0 #non-alphabet characters
C = 0 #Capital letters

workingPass = ""

import random
import string

def genPass(length, numeric, nonAlpha, caps):
    extra = length-(numeric+nonAlpha+caps)
    
    password = (''.join(random.choices(string.digits, k=numeric)))
    password = password+(''.join(random.choices(string.punctuation, k=nonAlpha)))
    password = password+(''.join(random.choices(string.ascii_uppercase, k=caps)))
    password = password+(''.join(random.choices(string.ascii_lowercase, k=extra)))
    return(password)

def randsort(password):
    password = ''.join(random.sample(password,len(password)))
    return(password)   
    
N = int(input("enter the number of numbers.> "))
X = int(input("enter the number of special characters.> "))
C = int(input("enter the number of capital letters.> "))
L = int(input("enter the total length of password.> "))
while L < (N+C+X):
    L = int(input("enter the total length of password, must be more than total of all previous inputs.> "))

workingPass = randsort(genPass(L,N,X,C))

print(workingPass)
