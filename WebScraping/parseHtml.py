# pip install beautifulsoup4
import bs4, requests

'''
# Example Code:
res = requests.get('https://www.ebay.ca/itm/Dyson-Official-Outlet-V8B-Cordless-Vacuum-Colour-may-vary-Refurbished/163025929449?_trkparms=%26rpp_cid%3D5e60145bd7246591bbee695a%26rpp_icid%3D5e60145bd7246591bbee6959&_trkparms=pageci%3A08d1c2d4-76fd-11eb-b808-32c73f019559%7Cparentrq%3Ad68057121770a9cc87bfbf54ffbee277%7Ciid%3A1')

res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

elems = soup.select('#prcIsum')

print(elems[0].text.strip())

'''


def getEbayPrice(productUrl):
    # Download Web page html
    res = requests.get(productUrl)
    # Check if download status
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # Select price
    elems = soup.select('#prcIsum')

    return elems[0].text.strip()

price = getEbayPrice('https://www.ebay.ca/itm/Dyson-Official-Outlet-V8B-Cordless-Vacuum-Colour-may-vary-Refurbished/163025929449?_trkparms=%26rpp_cid%3D5e60145bd7246591bbee695a%26rpp_icid%3D5e60145bd7246591bbee6959&_trkparms=pageci%3A08d1c2d4-76fd-11eb-b808-32c73f019559%7Cparentrq%3Ad68057121770a9cc87bfbf54ffbee277%7Ciid%3A1')
print('The price is ' + price)