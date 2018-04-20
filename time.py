from time import sleep
from termcolor import colored

handle = open("./lessons/lesson2.txt","r")
lst = handle.readlines()
def NewWords():
    for dummy_i in lst:
        print colored (dummy_i, 'green', attrs=['bold'])
        sleep(4)
        print "\n" * 2

while True:
    NewWords()
