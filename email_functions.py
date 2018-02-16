import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class gmailer:
	'''GMail sendmail class'''

	def __init__(self, givenSender = None, givenToken = None):
		if not givenSender or not givenToken:
			print('Email Config Not Loaded\nOne or more arguements not supplied\nCheck nova-config')
		else:
			self.sender = givenSender
			self.token = givenToken
			print('E-Mail Config Loaded')

	def send_email(self, to, subject, message):
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.ehlo()
		server.login(self.sender, self.token)
		msg = MIMEText(message)
		msg['Subject'] = subject
		msg['From'] = "bot@py"
		msg['To'] = to
		server.send_message(msg)
		server.quit()
