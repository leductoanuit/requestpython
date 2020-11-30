import requests 
import re
import lxml #parser html

url="https://courses.uit.edu.vn/login"
s=requests.session()
req=s.get(url)
logintoken=re.search(r"<input type=\"hidden\" name=\"logintoken\" value=\"(.*?)\">",str(req.content))
logintoken.group()
#print(logintoken[1])
data={
    'logintoken':str(logintoken[1]),
    'username':'1752xxxx',
    'password':'19xxxxxx',
    'rememberusername':'1'
    }

headers={
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding':'en-US,en;q=0.9,vi;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Content-Length':'108',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'
}
response=s.post("https://courses.uit.edu.vn/login/index.php",data=data,headers=headers)
print(response.status_code)
f = open('source.txt', mode='w', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
nd=str(response.content)
f.write(nd)
print(response.encoding)
