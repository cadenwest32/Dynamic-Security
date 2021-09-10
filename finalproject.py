#!/usr/bin/env python3

import subprocess as sub

#current_v = '2.4.46'

#Apache_v = str(sub.run(['apache2' , '-v']))

#PHP_V = str(sub.run(['php' , '-v']))

def update_a():
    print('Good job, your Apache server is updated to the latest version')  
    Question = input('Would you like to have the best settings available for this version? yes/no')
    if Question == 'no' or Question == 'n':
        print('Why not?')
     # message asking are you sure
    elif Question == 'yes' or Question == 'y':
        print('Okay cool')
            #next steps from below

def update_b():
    print('It looks like your Apache server is out of date')
    Question = input('Would you like to update your Apache server to the latest version with the best settings? yes/no')
    if Question == 'no' or Question == 'n':
        print('Do you want to get hacked?')
            #server vulnerable to attacks message
    elif Question == 'yes' or Question == 'y':
        print('Applying updates, and configuring optimal settings')
        updater = sub.Popen(['sudo', 'apt-get','install' ,'tree'], stdout = sub.PIPE) 
        #updater_confirm = str(sub.Popen(['sudo', 'apt-get', 'install', 'apache2'], stdout = sub.PIPE)    
        outputz=updater.communicate()
        print(outputz)
         #next steps
def main():
    Apache_v= str(sub.run(['apache2' , '-v'], stdout=sub.PIPE))
    PHP_v = str(sub.run(['php' , '-v']))
    print('------------------------')
    if '2.4.46' not in Apache_v:
        print('Success')    
        update_a()
    else:   
        update_b()
main()

#TODO move current_v (move all global variables into the function)
#TODO move apache_v and php_v into the main function 
#TODO move version check if statement into 'defmain' function
#TODO call the appropriate update function at the end and pass apache_v variable into functions (both)
#TODO ---TELL PYTHON TO TAKE BACK TGE OUTPUT INSTEAD OF KALI PROCESSING IT THE WAY IT DOES.......KEEP THINGS TEH SAME......SUBPROCESS  STANDARDOUT=_ CHEKC OUTPUT

