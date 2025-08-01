import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_address = "kartiksmittal2005@gmail.com"
to_address = "nikhilkumar21612161@gmail.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Test email"
msg['From'] = from_address
msg['To'] = to_address

# Create the message (HTML).
html = """\
hello
"""

# Record the MIME type - text/html.
part1 = MIMEText(html, 'html')

# Attach parts into message container
msg.attach(part1)

# Credentials
username = 'kartiksmittal2005@gmail.com'  
password = 'krfaegbdspfucqpk'

# Sending the email
## note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work
server = smtplib.SMTP('smtp.gmail.com', 587) 
server.ehlo()
server.starttls()
server.login(username,password)  
server.sendmail(from_address, to_address, msg.as_string())  
server.quit()
print('Mail send')