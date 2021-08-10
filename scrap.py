import requests
from bs4 import BeautifulSoup

# url = 'https://www.flipkart.com/poco-c3-lime-green-32-gb/p/itmdbc41b273ff7c?pid=MOBFVQJ5RMHGCWHF&lid=LSTMOBFVQJ5RMHGCWHFQV9OOD&marketplace=FLIPKART&srno=s_1_2&otracker=AS_Query_PredictiveAutoSuggest_7_0_na_na_na&otracker1=AS_Query_PredictiveAutoSuggest_7_0_na_na_na&fm=organic&iid=149e318b-9214-4460-b8e3-c2532c215bda.MOBFVQJ5RMHGCWHF.SEARCH&ssid=vttvik90qo0000001610444900772&qH=eb4af0bf07c16429'
url = 'https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_PredictiveAutoSuggest_7_0_na_na_na&otracker1=AS_Query_PredictiveAutoSuggest_7_0_na_na_na&as-pos=7&as-type=PREDICTIVE&suggestionId=mobiles&requestId=631ae882-33a5-4dc5-8b60-28e56a0c544b'

request = requests.get(url)

soup = BeautifulSoup(request.content, 'html.parser')

product_name = soup.find_all('div', attrs={'class': '_4rR01T'})

for name in product_name:
    print(name.text)

product_price = soup.find_all('div', attrs={'class': '_30jeq3 _1_WHN1'})

for name in product_price:
    print(name.text)

product_rating = soup.find_all('div', attrs={'class': '_3LWZlK'})



for name, price, rating in zip(product_name, product_price, product_rating):
    print(f'{name.text}: {price.text}: {rating.text}')

