import smtplib,ssl
from flask import Flask,request
#----Bunky Corporation-----
#Note this mail sender class/script is not asynchronous 
#as other parts of the program
#using this will block the async couroutines
#should be used only for couple of mail transfers
#NOT USED FOR BULK PROMOTIONAL EMAILS AT ONCE(10+)

#defaults
DEFAULT_SMTP_SERVER = "smtp.gmail.com"
DEFAULT_SMTP_PORT = 465

class MailSender:
    """simple mail sender class
       using python standard packages
    """

    def __init__(self,email,password,smtp_server=None,port=None):
        self.email = email
        self.password = password
        self.smtp_server = smtp_server or DEFAULT_SMTP_SERVER
        self.smtp_port =  port or DEFAULT_SMTP_PORT
        self.context = ssl.create_default_context()
    
    def send_mail(self,recipient,message="",subject=""):
        body = self.construct_message(message,subject)
        try:
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context=self.context) as server:
              server.login(self.email, self.password)
              server.sendmail(self.email, recipient, body)
        except smtplib.SMTPAuthenticationError:
            raise MailAuthenticationError("Username and Password not accepted.\
                Make sure Acess for Less Secure Apps Enabled\
                https://www.google.com/settings/security/lesssecureapps")
            

    
    def construct_message(self,message,subject):
        body = f'Subject: {subject}\n\n{message}'
        return body



class MailAuthenticationError(Exception):
    pass

mailsender = MailSender("your email", "your password/key")

#================FLASK API IMPLMENTATION============================

app = Flask(__name__)

@app.route('/send_mail', methods=['GET'])
def send_mail():
    print(request.args.get('recipient'),request.args.get('code'))
    mailsender.send_mail(request.args.get('recipient'),request.args.get('code'),"verification code")
    return "hello world"


app.run(host="0.0.0.0",port=1234)