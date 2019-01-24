import os
import smtplib


from_addr = 'kan@prontomarketing.com'
to_addr = 'kan@prontomarketing.com'

body = '''
New Releases and Sales on Steam.

Click the links below to check them out!
'''

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)

# heartbeat to smtp server
smtp_server.ehlo()

# start encryption session
smtp_server.starttls()

smtp_server.login('kan@prontomarketing.com',
                  os.environ.get('GOOGLE_APP_PASSWORD'))

smtp_server.sendmail(from_addr, to_addr, body)

smtp_server.quit()

print('Email sent successfully')
