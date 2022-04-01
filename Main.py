import SFTPFunctions
import pysftp


# retrieve the user's login info
print('What is the host name?\n')
host = input()
print('\nWhat is the username?\n')
username = input()
print('\nWhat is the password?\n')
password = input()
# establish sftp connection
sftpconnection = pysftp.Connection(host=host, username=username, password=password)
# check sftp connection
SFTPFunctions.handleCheck(SFTPFunctions.checkConnection(sftpconnection), sftpconnection)
# ask remote server for file/dir list
# compare directories
# determine if they're different
# determine which version is newer
# upload the new one
# verify the files using MD5
# delete the old versions if the sums match
# disconnect from remote server
