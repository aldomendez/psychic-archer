import urllib.request, urllib.parse, urllib.error

params = urllib.parse.urlencode({"txtFInicio":"2013-03-28","txtFFinal":"2013-03-29","optOpcion":"ambos","optgrouping":"dia"})
params = params.encode('utf-8')
# print(params)
page = urllib.request.urlopen('http://mexico/reports/starts_outs.php',params).read()
print(page)
