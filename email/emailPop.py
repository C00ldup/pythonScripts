import poplib
import imaplib

pop3server = ''
username = ''
password = ''
imapServer = imaplib.IMAP4_SSL(pop3server)
pop3Server = poplib.POP3_SSL(pop3server) # open connection
print (pop3Server.getwelcome()) #show welcome message
print (imapServer.login(username, password))
print()
pop3Server.user(username)
pop3Server.pass_(password)

pop3info = pop3Server.stat() #access mailbox status
mailcount = pop3info[0] #total email
print("Total no. of Email : " , mailcount)
print(pop3Server.list())
print(imapServer.select('Inbox'))
tmp, data = imapServer.search(None, 'ALL')
print(tmp)
#print(pop3Server.retr(1))
#print(pop3Server.dele(1))
'''
print ("\n\nStart Reading Messages\n\n")
for i in range(mailcount):
    for message in pop3Server.retr(i+1)[1]:
        print(pop3Server.retr(i+1)[1].index(message))
        print(message.decode('utf-8'))
'''
pop3Server.quit()
imapServer.close()