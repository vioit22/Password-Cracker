from random import *
import os
root = input("Password Cracker developed by Vio IT! Hit Enter the continue")
u_pwd = input("Enter the password:")
pwd=['1', '2', '3', '4', '5', '6', '7', '8', '9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

pw=""
while(pw!=u_pwd):
    pw=""
    for letter in range(len(u_pwd)):
        guess_pwd = pwd[randrange(0, 1)]
        guess_pwd = pwd[randrange(0, 2)]
        guess_pwd = pwd[randrange(0, 3)]
        guess_pwd = pwd[randrange(0, 4)]
        pw=str(guess_pwd)+str(pw)
        print(pw)
        print("Cracking Password is in Progress... Please Wait! It takes several minutes or hours depending your password entered!")
        os.system("cls")
print("Your Password Is:", pw)
root = input("It encounter problem with his program, please contact me by mail vioit@hotmail.com! Press Enter to close the program!")