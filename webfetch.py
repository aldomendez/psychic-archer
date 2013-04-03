import urllib.request, urllib.parse, urllib.error, re
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

def showResults(pattern,searchItem):
	m = pattern.search(page)
	if m:
			for result in pattern.finditer(page):
				fecha, tag, mov, value = result.groups()
				print(">> {:14s} {:10s} {:4s} {:4s}".format(tag,fecha,mov,value))
	else:
		print('No match',searchItem)

def fetchResults(code):
	regex = 'MZ.*(\d{4}-\d{2}-\d{2}).*(' + code + ').+(DONE).*>(\d+)'
	# print(regex)
	pattern = re.compile(regex, re.MULTILINE)
	showResults(pattern,code)	

hoy = ""
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

if workingFromWeb:
	params = encodeParams()
	page = readWeb('http://mexico/reports/starts_outs.php',params)
else:
	page = readFile('starts_outs.txt')

fetchResults('LR4 SHIM ROSA')
fetchResults('LR4G1WALPS')