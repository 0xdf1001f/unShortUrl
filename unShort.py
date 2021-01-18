用来将URL短链接还原为原始的链接
使用了免费的API，因为很多APT的短链失效很快，失效后直接Request会出问题
Python3.8


#将txt文本内的所有短链展开
import time
import requests
def geturl(apiUrl,queryUrl):
    res = requests.get(apiUrl,params = queryUrl)	
    url = res.text
    return url

data = []
expandUrl = []
for line in open('C:\\Users\\User\\Desktop\\shortURL.txt'):	#按行读取文件
	line=line.rstrip("\n")						#去除每行末尾'\n'
	data.append(line)							#将文件内url写为list
length = len(data)								#判断行数，多少个url
for i in range(0,length):
	queryUrl = {'url':data[i]}
	apiUrl = 'http://expandurl.com/api/v1/'
	print(geturl(apiUrl,queryUrl))
	time.sleep(37)							#API限制每小时100次
