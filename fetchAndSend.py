import urllib.request, urllib.parse, urllib.error, re, smtplib, datetime

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
	page = urllib.request.urlopen(page,encodedParams).read()asd fwgej}
	return page.decode('utf-8')

def encodeParams():
	global hoy,ayer,manana
	d = datetime.datetime.now()
	if d.hour > 7:
		inicio = ayer
		final = hoy
	else:
		inicio = hoy
		final = manana
	params = urllib.parse.urlencode({"txtFInicio":str(inicio),"txtFFinal":str(final),"optOpcion":"ambos","optgrouping":"dia"})
	params = params.encode('utf-8')
	return params

def getResults(pattern):
	m = pattern.findall(page)
	return m

def parseREGEX(code):
	regex = 'MZ.*(\d{4}-\d{2}-\d{2}).*(' + code + ').+(DONE).*>(\d+)'
	pattern = re.compile(regex, re.MULTILINE)
	return pattern	

def getDONES(code):
	pattern = parseREGEX(code)
	result = getResults(pattern)
	if result:
		# print(result)
		for r in result:
			fecha, tag, mov, value = r
			# print(tag)
		fecha, tag, mov, value = result[0]
		return ">> {:14s} {:10s} {:4s} {:4s}".format(tag,fecha,mov,value)
	else:
		return 'No match for ' + code

def appendDonesToMail(code):
	global dones
	dones = dones + getDONES(code) + '\n'

def initDates():
	global hoy,ayer,manana
	hoy = datetime.date.today()
	ayer = hoy + datetime.timedelta(days = -1)
	manana = hoy + datetime.timedelta(days=1)

###################################
# Si trabajo desde CyOptics sera True
# Si quiero probar REGEX sera False
# Si quiero hacer casi cualquier otra prueba sera False
workingFromWeb = False
initDates()
dones = ""
if workingFromWeb:
	params = encodeParams()
	page = readWeb('http://mexico/reports/starts_outs.php',params)
else:
	page = readFile('starts_outs.txt')

#map(print, ['LR4 SHIM ROSA','LR4G1WALPS'])

[appendDonesToMail(x) for x in ['LR4 SHIM ROSA','LR4G1WALPS']]

####################################################
# Configuracion del servicio
def sendMail():
	FROMADDR = "aldomendez86@gmail.com"
	LOGIN    = "aldomendez86@gmail.com"
	PASSWORD = "dsorokzerkmodtne"
	TOADDRS  = ["aldomendez86@gmail.com",""]
	SUBJECT  = "RE:OUTS LR4"
	 
	msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
	       % (FROMADDR, ", ".join(TOADDRS), SUBJECT) )
	msg += "Dones de " + str(hoy) + "\n\n" + dones

	writeToFile("errorLog.txt",msg)

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.set_debuglevel(1)
	server.ehlo()
	server.starttls()
	server.login(LOGIN, PASSWORD)
	server.sendmail(FROMADDR, TOADDRS, msg)
	server.quit()

sendMail()