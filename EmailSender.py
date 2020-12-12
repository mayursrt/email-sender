import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = '<Name>'
email['to'] = '<recievers_email>'
email['subject'] = '<email_subject>'

email.set_content('email_body')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:#set up the smtp server according to your email client
	smtp.ehlo()
	smtp.starttls()
	smtp.login('<senders_email_id>', '<senders_password>')
	smtp.send_message(email)
	print('Message Sent')
	smtp.quit()

	#turn on less secure apps from google account