#!/usr/bin/env python3

import subprocess as sub

Apache_v = sub.run(["apache2", "-v"])
PHP_v = sub.run(["php", "-v"])
print(Apache_v)
print(PHP_v)
current_v = "2.4.48"
def update_A():
    if current_v in Apache_v:
        print('Good job, your Apache server is updated to the latest version')
    while True:
        Question = input('Would you like to have the best settings available for this version? yes/no')
        if Question == 'no' or Question == 'n':
            print('Why not?')
            #message asking are you sure
        elif Question == 'yes' or Question == 'y':
            print('Okay cool')
            #next steps from below
        else:
            print('Please answer with yes or no')
    else:
        while True:
        Question = input('Would you like to update your Apache server to the latest version with the best settings? yes/no')
        if Question == 'no' or Question == 'n':
            print('Do you want to get hacked?')
           #server vulnerable to attacks message
        elif Question == 'yes' or Question == 'y':
            print("Ok here's the next steps")
            #next steps
        else:
            print('Please answer with yes or no')


