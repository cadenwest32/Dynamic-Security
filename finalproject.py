#!/usr/bin/env python3

import subprocess as sub
import sys

def update_a(config_file, config_file_2):
    print('Good job, your Apache server is updated to the latest version')
    while True:
        Question = input('Would you like to have the best settings available for this version? yes/no ')
        if Question == 'no' or Question == 'n':
            print('Why not?')
     # message asking are you sure
        elif Question == 'yes' or Question == 'y':
            print('Okay cool')
            usrcheck()
            #config_file = sys.argv[1]
            #config_file_2 = sys.argv[2]
            whitelist(config_file)
            servertoken(config_file)
            htaccess(config_file_2)
            break
            #next steps from below
        else: 
            print('Please respond with yes or no')

def update_b():
    print('It looks like your Apache server is out of date')
    while True:
        Question = input('Would you like to update your Apache server to the latest version with the best settings? yes/no ')    
        if Question == 'no' or Question == 'n':
            print('Do you want to get hacked?')
            #server vulnerable to attacks message
        elif Question == 'yes' or Question == 'y':
            print('Applying updates, and configuring optimal settings')
            updater = sub.Popen(['sudo', 'apt-get','install' ,'apache2', '-y'], stdout = sub.PIPE)    
            updatedd=updater.communicate()
            print(updatedd)
            break
        #next steps
    else:
        print('Please respond with yes or no')

def usrcheck():
    psout = sub.run(['ps', '-aux'], stdout=sub.PIPE)
    psout = psout.stdout.decode('UTF-8')
    #print(psout)
    psout = psout.split('\n')
    for line in psout:
        #print(line)
        if 'apache' in line:
            #print(line)
            if 'root' in line:
                print('Incorrect settings, please run apache2 as an unprivilaged user')
            else:
                print('Correct settings detected, apache is running as an unprivailaged user')

def whitelist(location):
    with open(location) as open_file:
        check = False
        while check == False:
            for line in open_file:
                if line.startswith('Require ip'):
                    print('Correct settings detected, you have successfully whitelisted your ip address')
                    check = True
                    break
               #else:
            if check == False:
                print('Refer to configuration number 3 of Apache patches document for whitelisting your ip address')
                break

def servertoken(location_2):
    with open(location_2) as open_file_2:
        check = False
        while check == False:
            for line in open_file_2:
                if line.startswith('ServerTokens ProductOnly'):
                    print('Correct settings detected, you have successfully hid the server token')
                    check = True
                    break
            if check == False:
                print('Refer to configuration number 4 of the Security Best Practices document for hiding server tokens')
                break
def htaccess(location_3):
    with open(location_3) as open_file_3:
        check = False
        while check == False:
            for line in open_file_3:
                if line.startswith('AllowOverride None'):
                    print('Correct settings detected, you have successfully blocked vulnerable configurations')
                    check = True
                    break
            if check == False:
                print('Refer to configuration number 2 of the Security Best Practices document for blocking .htaccess')
                break
            





def main():
    Apache_v= str(sub.run(['apache2' , '-v'], stdout=sub.PIPE))
    PHP_v = str(sub.run(['php' , '-v']))
    #usrcheck()
    config_file = sys.argv[1]
    config_file_2 = sys.argv[2]
    #whitelist(config_file)
    #servertoken(config_file_2)
    if '2.4.48' in Apache_v:    
        update_a(config_file, config_file_2)
    else:   
        update_b()
main()

#TODO move current_v (move all global variables into the function)
#TODO move apache_v and php_v into the main function 
#TODO move version check if statement into 'defmain' function
#TODO call the appropriate update function at the end and pass apache_v variable into functions (both)
#TODO ---TELL PYTHON TO TAKE BACK TGE OUTPUT INSTEAD OF KALI PROCESSING IT THE WAY IT DOES.......KEEP THINGS TEH SAME......SUBPROCESS  STANDARDOUT=_ CHEKC OUTPUT

