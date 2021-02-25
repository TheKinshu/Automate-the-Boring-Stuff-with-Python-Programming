import smtplib # simple mail transfer protocal library

# Information for domain server
# Provider                  SMTP server Domain Name
# Gmail                     smtp.gmail.com
# Outlook.com/hotmail.com   smtp.mail.outlook.com
# Yahoo Mail                smtp.mail.yahoo.com
# AT&T                      smtp.mail.att.net (Port 465)
# Comcast                   smtp.comcast.net
# Verizon                   smtp.verizon.net (Port 465)

conn = smtplib.SMTP('smtp.gmail.com', 587)

conn.ehlo() # This start the connections
conn.starttls() # Start tls encryption * Most modern email domain require this

# Connecting account
conn.login('youremail@gmail.com', 'khkhycskynqmiyiv')

#              From                       To                   Body
conn.sendmail('youremail@gmail.com', 'toEmail@gmail.com', 
                'Subject: Test2...\n\n This is a test email from myself.\n So long, and farewell.\n\nKel')

# Disconnecting from smtp server
conn.quit()

