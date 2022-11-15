import os
import urllib.request
SERVERPUSHKEY = os.environ["SERVERPUSHKEY"]
url="https://api2.pushdeer.com/message/push?pushkey=" + SERVERPUSHKEY + "&text=❤️周末到了给父母回个电话吧❤️"
req=urllib.request.Request(url)
resp=urllib.request.urlopen(req)
data=resp.read().decode('utf-8')

print(data)

