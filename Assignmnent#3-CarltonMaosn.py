import sys
import statistics
import time
from tqdm import tqdm
from tabulate import tabulate
from termcolor import colored, cprint
import webbrowser

# Final Project Software Engineering

## The different Gas Stations ##

# This make the program stop executing for 2 seconds to create the delay

## To help Personalize the Program in a way we are going to create a greeting
name = input('Who do I have the pleasure of speaking with ?  ')
if name != 'Amar':
    if name != 'Brandy':
        print("Hello " + name)
        time.sleep(0.5)
        print("Thank You For Using the Gas Station App " + name)
        time.sleep(1)
        print("please Let Us Know how the app is By rating once the app has executed")
        time.sleep(3)
        ## Login Script Below VERY BASIC NOT CONNECTED TO ANY DB
        print("The Credentials Are below To access")
##This will allow the program to continue

table2 = ['Username:', 'username'], ['password:', 'password']
print(tabulate(table2, headers='firstrow', tablefmt='grid'))
## will comeback and edit the new feature !!

CorrectUsername = "username"
CorrectPassword = "password"

loop = 'true'
while (loop == 'true'):
    username = input("Please enter your username: ")
    if (username == CorrectUsername):
        password = input("Please enter your password: ")
    if (password == CorrectPassword):
        print("Logged in successfully as " + name)
        loop = 'false'
    else:
        print("Password incorrect!")
else:
    print("Username correct!")

##BREAK THIS##
from colorama import init

init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

cprint(figlet_format('Gas Station APP!', font='starwars'),
       'yellow', attrs=['bold'])

while True:
    # your code
    list = ["Shell", "Texaco", "BP", "Sams Club", "Kroger Gas", "Cosco Gas"]
    cprint('\nThe Gas Stations In the Area', 'green', attrs=['blink'])
    time.sleep(0.5)
    print(list[0])
    print(list[1])
    print(list[2])
    print(list[3])
    print(list[4])
    print(list[5])
    cont = input("Would you like to see the prices for the listed gas stations yes/no > ")
    while cont.lower() not in ("yes", "no"):
        cont = raw_input("Another one? yes/no > ")
    if cont == "yes":
        time.sleep(1)
       
    if cont == "no":
        print("Thanks for using the app, to continue using restart to get the full experince ")
    
    ##This creates the loading bar for the table using the Module tabulate
    for i in tqdm(range(100),
                  desc="Loading???",
                  ascii=False, ncols=75):
        time.sleep(0.05)

    table1 = [['Gas Station Name', 'Price'], ['Shell', '3.23'], ['Texaco', '3.49'], ['BP', '2.98'],
              ['Sams Club', '3.02'], ['Kroger Gas', '3.12'], ['Cosco Gas', '3.91']]
    print(tabulate(table1, headers='firstrow', tablefmt='grid'))
    break

print("Complete.")
print("Moving Along......")



while True:
    # adaption HAHAAHHA

    # I Like a lot of color THIS IS NOT NO BASIC  PROGRAWM HAHAHA Lol IT IS ##
    print("\033[1;32;40m You now Have the Prices as well as the Specific gas Stations \n ")
    cont = input(
        "\033[1;37;40m  Would you like to see the average price of Premium Gas for the listed gas stations yes/no > \n ")
    while cont.lower() not in ("yes", "no"):
        cont = raw_input("Another one? yes/no > ")
    if cont == "yes":
        time.sleep(1)
        break
    if cont == "no":
        print("Thank you for using the Program, to access More Features of the Program conintue through")
    
##This creates the loading bar for the table using the Module tabulate
print("The Most Expensive cost of gas is... ")
## COME BACKAND FIX THS S
list1 = [3.23, 3.49, 2.98, 3.02, 3.12, 3.91]
list1.sort()
print("\033[3;37;40m", list1[-1])
print("Belonging To  Cosco Gas !! Stay Away !")
time.sleep(2)
print("loading...........")
print(
    "Not Local to the area of macon? No worries, Input The Gas station prices For your Area and ill do the calculations for you")
## Ideas below Here for calculator

num = int(input('How many Gas Stations: '))
total_sum = 0
for n in range(num):
    numbers = float(input('Enter Price : '))
    total_sum += numbers
avg = total_sum / num
print('Average of ', num, ' Gas Stations is :', avg)
time.sleep(2)
print("Thank you So much for a Great Semester" + name)
print("Dont Go just yet their is One More Part" + name)

for i in tqdm(range(100),
                  desc="Loading???",
                  ascii=False, ncols=75):
        time.sleep(0.03)
        break
print("Follow Me on Linked-IN")
time.sleep(3)
webbrowser.open("https://www.linkedin.com/in/carlton-mason-bb7b901b5/", new=1)
init(strip=not sys.stdout.isatty())

from termcolor import cprint
from pyfiglet import figlet_format

cprint(figlet_format('Good Bye !!', font='starwars'),
       'yellow', attrs=['bold'])

 
## Thinking about adding a rating system that would report the name intentiy to know who rated the system.##