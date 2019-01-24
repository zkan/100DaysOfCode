import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


from_addr = 'kan@prontomarketing.com'
to_addr = 'kan@prontomarketing.com'
cc = ['kan+cc@prontomarketing.com',]
bcc = ['kan+bcc@prontomarketing.com',]

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Cc'] = ','.join(cc)
msg['Subject'] = 'New Releases and Sales on Steam'

body = '''
New Releases and Sales on Steam.

Click the links below to check them out!
'''
msg.attach(MIMEText(body, 'plain'))

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)

# heartbeat with smtp server
smtp_server.ehlo()

# start encryption session
smtp_server.starttls()

smtp_server.login('kan@prontomarketing.com',
                  os.environ.get('GOOGLE_APP_PASSWORD'))

text = msg.as_string()
print(text)

smtp_server.sendmail(from_addr, [to_addr] + cc + bcc, text)

smtp_server.quit()

print('Email sent successfully')
