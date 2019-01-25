import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from hacker_news_api import get_top_10_best_stories


from_addr = 'kan@prontomarketing.com'
to_addr = 'kan@prontomarketing.com'
cc = ['kan+cc@prontomarketing.com',]
bcc = ['kan+bcc@prontomarketing.com',]

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Cc'] = ','.join(cc)
msg['Subject'] = 'Top 10 Best Stories on Hacker News'

results = get_top_10_best_stories()
body = '10 Best Stories on Hacker News.\n\n'
for index, each in enumerate(results, 1):
   body += f'{index}. {each.title} - {each.url}\n'

msg.attach(MIMEText(body, 'plain'))

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)

# heartbeat to smtp server
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
