import urllib.request, urllib.parse, urllib.error, re
#f = open('starts_outs.txt', 'w')
params = urllib.parse.urlencode({"txtFInicio":"2013-03-28","txtFFinal":"2013-03-29","optOpcion":"ambos","optgrouping":"dia"})
params = params.encode('utf-8')
# print(params)
page = urllib.request.urlopen('http://mexico/reports/starts_outs.php',params).read()
# print(page)
decodedPage = page.decode('utf-8')
# f.write(decodedPage)
# f.close()
pROSA = re.compile('0010536020; LR4 SHIM ROSA</TD><TD nowrap>LR4 SHIM ROSA</TD><TD nowrap>LR4</TD><TD nowrap>SFCREL</TD><TD nowrap>', re.MULTILINE)
m = pROSA.match(decodedPage)
if m:
    print('Match found: ', m.group())
else:
    print('No match')
# print(decodedPage)
