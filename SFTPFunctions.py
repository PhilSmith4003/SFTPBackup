import os


def checkConnection(connection):
    # function that takes a pysftp.connection object and verifies the connection
    localdirs = os.getcwd()
    remotedirs = connection.pwd
    # get local and remote directories and compare the location to see if the connection succeeded
    if localdirs != remotedirs:
        return True
    else:
        return False


def handleCheck(connectioncondition, connection):
    if connectioncondition:
        print('Connection Succeeded!\n')
    else:
        print('Connection Failed, Try again? (Y/N)\n')
        checkagain = input()
        print('\n')
        if checkagain == 'y' or 'yes':
            handleCheck(checkConnection(connection))
        elif checkagain == 'n' or 'no':
            print('Exiting Program.\n')
            quit()
