import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = '<Name>'
email['to'] = '<recievers_email>'
email['subject'] = '<email_subject>'


email.set_content(html.substitute(name = 'TinTin', age = '23'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('<email id>', '<password>')
	smtp.send_message(email)
	print('Message sent')
	smtp.quit()

	#turn on less secure apps from google account