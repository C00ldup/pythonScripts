import poplib, imaplib, email, getpass
import pprint
import mailparser

class Email:
    server = None
    protocollo = None

    def __init__(self, protocollo="imap"):
        host = input("host: ")
        username = input("username: ")
        password = getpass.getpass()

        try:
            if protocollo == "imap":
                self.server = imaplib.IMAP4_SSL(host)
                self.protocollo = self.server.__class__.__name__
                print("Connection Object : {}".format(self.server))
                print("Login: {}".format((self.server.login(username, password)[1][0]).decode("UTF-8")))
            elif protocollo == "pop":
                self.server = poplib.POP3_SSL(host)
                self.protocollo = self.server.__class__.__name__
                self.server.user(username)
                self.server.pass_(password)
                print("Connection Object : {}".format(self.server))
                print("Login: {}".format(self.server.getwelcome().decode("UTF-8")))
        except Exception as e:
            print("ErrorType : {}, Error : {}".format(type(e).__name__, e))
            self.server = None
            self.protocollo = None

    def getLastEmail(self):
        try:
            if self.server.__class__.__name__ == "IMAP4_SSL":
                print(self.server.select()[1][0].decode("UTF-8"))
                tmp, data = self.server.fetch(self.server.select()[1][0], '(RFC822)')
                tmp, data = self.server.fetch(b'2', '(RFC822)')
                mail = mailparser.parse_from_bytes(data[0][1])
                print(mail.subject)
                print(mail.text_plain)
                print(mail.attachments)
                #pprint.pprint(data[0][1].decode("UTF-8"))                    
                return True
            elif self.server.__class__.__name__ == "POP3_SSL":
                print("pop")
        except Exception as e:
            print(e)

    def getEmails():
        pass
    
    def getUnread(self):
        try:
            if self.server.__class__.__name__ == "IMAP4_SSL":
                self.server.select(readonly=1) # Select inbox or default namespace
                (retcode, messages) = self.server.search(None, '(UNSEEN)')
                if retcode == 'OK':
                    for num in messages[0].decode("UTF-8").split(' '):
                        typ, data = self.server.fetch(num,'(RFC822)')
                        msg = email.message_from_string(data[0][1].decode("UTF-8"))
                        typ, data = self.server.store(num,'-FLAGS','\\Seen')
                        if retcode == 'OK':
                            print(data,'\n',30*'-')
                            print(msg)
        except Exception as e:
            print(e)

    def deleteEmail(self):
        # self.server.__class__.__name__ == "IMAP4_SSL":
        if self.server.__class__.__name__ != "POP3_SSL":
            print("Need pop protocol")
            return False
        
    def getMsgs(self):
        self.server.select('Inbox')
        typ, data = self.server.search(None,'(UNSEEN SUBJECT "%s")' % subject)
        for num in data[0].split():
            typ, data = self.server.fetch(num,'(RFC822)')
            msg = email.message_from_string(data[0][1])
            typ, data = self.server.store(num,'-FLAGS','\\Seen')
            yield msg

    def getAttachment(msg,check):
        for part in msg.walk():
            if part.get_content_type() == 'application/octet-stream':
                if check(part.get_filename()):
                    return part.get_payload(decode=1)
        
emailImap = Email()
emailPop = Email("pop")

emailImap.getLastEmail()
#emailPop.getLastEmail()