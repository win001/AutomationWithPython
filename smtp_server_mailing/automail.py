import smtplib

# Define the email parameters
from_address = "user_name@gmail.com"
to_address = "user_name@gmail.com"
subject = "Hello, buddy!"
body = "Kya hall chal this email is send by a script :)"

# Construct the email message
message = f"Subject: {subject}\n\n{body}"

# Connect to the SMTP server (465)
smtp_server = smtplib.SMTP('smtp.gmail.com', 587)

smtp_server.connect("smtp.gmail.com",587)
smtp_server.ehlo()
smtp_server.starttls()
smtp_server.ehlo()

# Login to the SMTP server (if necessary)
smtp_server.login("v", "password")

# Send the email
smtp_server.sendmail(from_address, to_address, message)

# Disconnect from the SMTP server
smtp_server.quit()

# try:
#    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
#    smtpObj.login("username", "password")
#    smtpObj.sendmail(from_address, to_address, message)
#    smtpObj.quit()      
#    print("Successfully sent email")
# except SMTPException:
#    print ("Error: unable to send email")