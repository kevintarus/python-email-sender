import smtplib

EMAIL_ADDRESS = 'example@gmail.com'
EMAIL_PASSWORD = 'exampleexampleexample'

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.ehlo()

	smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

	subject = 'EMAILS WITH PYTHON'
	body = 'You can send yourself emails with python'
	msg = f'Subject: {subject}\n\n{body}'

	smtp.sendmail('example@gmail.com', 'example1@gmail.com', msg)
