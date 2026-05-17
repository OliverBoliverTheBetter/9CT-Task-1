#This is THE code of all time
#Menu options: view all my data, visualise the data, search for the data, edit the data, exit the data
#imports
import time as tcorp
from data_module import *
#functions
def TheMain():
    
    while True:
        print("yo wassup this is the DATA you gotta believe me\n")
        tcorp.sleep(1)
        print("The choices:\n1. View all my data\n2. Visualise all my data\n3. Search for the data\n4. Edit my data\n5. Exit this lovely Juvely program.")
        tcorp.sleep(3)
        try:
            thechoicening = int(input("\nYou  must now decide your fate.\n"))
        
        except:
            print("\nStupid dumb dumb stupid fart face idiot\n")
        
        if thechoicening == 1:
            print("All the data coming up!\n") #Future me has helped :thumbsup:
            tcorp.sleep(2)
            DisplayData()
        elif thechoicening == 2:
            print('Visualised data coming up!\n') #PLEASE FOR THE LOVE OF GOD FUTURE ME HELP
        
        elif thechoicening == 3:
            print('Find my data\n') #PLEASE FOR THE LOVE OF GOD FUTURE ME HELP

        elif thechoicening == 4:
            print("Whats wrong with my data :(\n") #PLEASE FOR THE LOVE OF GOD FUTURE ME HELP

        elif thechoicening == 5:
            print('Do you really want me to die?\n')
            break
        
        else:
            print("Your so mean why didnt you choose ")
        


#The happening area
TheMain()