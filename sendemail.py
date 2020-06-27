import smtplib
sender_email = "nishantsingh70600@gmail.com"
receiver_email = "nishantsingh9526@gmail.com"
password = "nishu70600"
message = "Your code is working good"
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,password)
print('Login Successfullt')
server.sendmail(sender_email,receiver_email,message)
print("Email has been sent to", receiver_email)
server.quit()
