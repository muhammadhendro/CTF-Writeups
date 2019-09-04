

```
import requests
import base64

s = requests.Session()
site = "http://203.201.167.78:10001/index.php"
res = s.get(site)
headers = res.headers["Get-flag"]
print(headers)
decode = base64.b64decode(headers)
print(decode)
payload = {"IndoSecurity": decode}
r = s.post(site, data=payload)
print(r.text)

```