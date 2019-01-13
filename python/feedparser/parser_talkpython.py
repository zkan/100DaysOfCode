import os

import feedparser
import sendgrid
from sendgrid.helpers.mail import Content, Email, Mail


FEED_FILE = 'newreleases_talkpython.xml'

feed = feedparser.parse(FEED_FILE)

if 'title' in feed.entries[0]:
    for entry in feed.entries:
        print(f'{entry.published} - {entry.title}: {entry.link}')

print('Emailing the latest episode..')
latest_episode = feed.entries[0]
content = f'{latest_episode.published} - {latest_episode.title}: ' \
    f'{latest_episode.link}'

sg = sendgrid.SendGridAPIClient(
    apikey=os.environ.get('SENDGRID_API_KEY')
)
from_email = Email('kan@prontomarketing.com')
to_email = Email('kan@prontomarketing.com')
subject = 'Latest Episode from TalkPython!'
content = Content('text/plain', content)
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
if response.status_code == 202:
    print('Done!')
