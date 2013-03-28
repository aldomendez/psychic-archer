import smtplib
 
FROMADDR = "aldomendez86@gmail.com"
LOGIN    = "aldomendez86@gmail.com"
PASSWORD = "dsorokzerkmodtne"
TOADDRS  = ["amendez@cyoptics.com", "tlugo@cyoptics.com"]
SUBJECT  = "Python Mail Service Test"
 
msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
       % (FROMADDR, ", ".join(TOADDRS), SUBJECT) )
msg += "Prueba de envio de correos, usando cuenta de correo externo en Gmail\r\n"
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(LOGIN, PASSWORD)
server.sendmail(FROMADDR, TOADDRS, msg)
server.quit()
