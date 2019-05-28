import requests

#req = requests.get('http://raspberrypidpm2.ddns.net/SitioWebFinal')

for i in range(10000):
    req = requests.get('http://raspberrypidpm2.ddns.net/SitioWebFinal')

    print req.status_code


print()
