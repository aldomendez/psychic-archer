import urllib.request, urllib.parse, urllib.error, re, smtplib
from datetime import date,timedelta

def readFile(file):
	f = open(file, 'r')
	text = f.read()
	f.close()
	return text	

def writeToFile(file,content):
	try:
		f = open(file,'w')
		f.write(content)
		f.close()
	except :
		raise
	
def readWeb(page,encodedParams):
	page = urllib.request.urlopen(page,encodedParams).read()
	return page.decode('utf-8')

def encodeParams():
	params = urllib.parse.urlencode({"txtFInicio":"2013-03-28","txtFFinal":"2013-03-29","optOpcion":"ambos","optgrouping":"dia"})
	params = params.encode('utf-8')
	return params

def getResults(pattern):
	m = pattern.findall(page)
	return m

def parseREGEX(code):
	regex = 'MZ.*(\d{4}-\d{2}-\d{2}).*(' + code + '.*)<.+(DONE).*>(\d+)'
	pattern = re.compile(regex, re.MULTILINE)
	return pattern	

def getDONES(code):
	pattern = parseREGEX(code)
	result = getResults(pattern)
	if result:
		print(result)
		for r in result:
			fecha, tag, mov, value = r
			print(tag)
		fecha, tag, mov, value = result[0]
		return ">> {:14s} {:10s} {:4s} {:4s}".format(tag,fecha,mov,value)
	else:
		return 'No match for ' + code

def appendDonesToMail(code):
	global dones
	dones = dones + getDONES(code) + '\n'

def manageDates():
	global hoy
	hoy = date.today()
	ayer = hoy + timedelta(days = -1)
	manana = hoy + timedelta(days=1)
	#print(ayer,hoy,manana)

manageDates()
print(hoy)
###################################
# Si trabajo desde CyOptics sera True
# Si quiero probar REGEX sera False
# Si quiero hacer casi cualquier otra prueba sera False
workingFromWeb = False
dones = ""
if workingFromWeb:
	params = encodeParams()
	page = readWeb('http://mexico/reports/starts_outs.php',params)
else:
	page = readFile('starts_outs.txt')

#map(print, ['LR4 SHIM ROSA','LR4G1WALPS'])
[appendDonesToMail(x) for x in ['LR4 SHIM ROSA','LR4G1WALPS','E2560S']]
print(dones)
####################################################
# Configuracion del servicio

# FROMADDR = "aldomendez86@gmail.com"
# LOGIN    = "aldomendez86@gmail.com"
# PASSWORD = "dsorokzerkmodtne"
# TOADDRS  = ["aldomendez86@gmail.com"]
# SUBJECT  = "OUTS LR4"
 
# msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
#        % (FROMADDR, ", ".join(TOADDRS), SUBJECT) )
# msg += "Dones de " + str(hoy) + "\n\n" + dones

# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.set_debuglevel(1)
# server.ehlo()
# server.starttls()
# server.login(LOGIN, PASSWORD)
# server.sendmail(FROMADDR, TOADDRS, msg)
# server.quit()