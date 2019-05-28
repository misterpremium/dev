import requests
req = requests.get('http://raspberrypidpm2.ddns.net')

print req.encoding
print req.status_code
print req.elapsed
print req.url


print req.history

print req.headers['Content-Type']

