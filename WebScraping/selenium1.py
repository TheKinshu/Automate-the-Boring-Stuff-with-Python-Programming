# pip install selenium
from selenium import webdriver

browser = webdriver.Chrome('E:\\Study\\AutomateCourse\\WebScraping\\chromedriver')
browser.get('https://automatetheboringstuff.com')

elem = browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > ul:nth-child(21) > li:nth-child(1) > a')
elem.click()

browser.get('https://www.google.com')


searchElem = browser.find_element_by_css_selector('body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')
searchElem.send_keys('doggo')
searchElem.submit()

# browser.back() Back a page
# browser.forward() Next page
# browser.refresh() Refresh current page
# browser.quit() This close the browser