#Ken Leam G. Gamboa
#BSCPE 1-5
#This is a program that decrypts some specified characters from the user's input.

#Print an introduction:
import time
time.sleep(2)
print(("\033[1m" + "Hi there! This is a program that can decipher the encrypted message behind the user's input.".center(100)))
#ask for user's input:
time.sleep(2)
user_input = input("\nInput the encrypted message: ")
user_output = ""

#check each character from the user's input:
for i in range(len(user_input)):
    #if there's "*", change to "a":
    if user_input[i] == "*":
        user_output += "a"
    #if there's "&", change to "e":
    elif user_input[i] == "&":
        user_output += "e"  
    #if there's "#", change to "i":
    elif user_input[i] == "#":
        user_output += "i"
    #if there's "+", change to "o":
    elif user_input[i] == "+":
        user_output += "o"
    #if there's "!", change to "u":
    elif user_input[i] == "!":
        user_output += "u"   
    #transfer remaining characters on the output:
    else:
        user_output += user_input[i]

#Print the decrypted message:
import pyfiglet
import time
for j in range(3):
    print("\n.")
time.sleep(1)
MESSAGE_PROMPT = "Decrypted Message: \n"
print("\n\033[1m" + "\033[35m"+ MESSAGE_PROMPT)
time.sleep(1)
print("\033[35m" + "\033[1m" + pyfiglet.figlet_format(user_output, font = "larry3d"))

#Print an ender for the program
PROGRAM_ENDER = "END"
time.sleep(3)
print ("\n" + "\033[1m" + PROGRAM_ENDER.center(90, "="))
