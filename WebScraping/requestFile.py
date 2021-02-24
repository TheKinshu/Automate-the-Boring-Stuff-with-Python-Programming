# requests module is 3rd party so you will have to install it 
# pip install requests

import requests
res = requests.get('http://automatetheboringstuff.com/files/rj.txt')

if res.status_code == 200:
    print('Success')
elif res.status_code == 404:
    raise Exception('Link was not available')


print(res.text[:500])


playFile = open('.\\WebScraping\\RomeoAndJuliet.txt', 'wb')

for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()