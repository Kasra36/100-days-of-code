from bs4 import BeautifulSoup
import requests

WEBPAGE = 'https://appbrewery.github.io/Zillow-Clone/'

class WebData:
    def __init__(self):
        self.links = []
        self.prices = []
        self.addresses = []
        self.get_data()

    def get_data(self):
        try:
            response = requests.get(WEBPAGE)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            link_tags = soup.find_all(name='a', class_='property-card-link')
            self.links = [link.get('href') for link in link_tags if link.get('href')]

            price_tags = soup.find_all(name='span', class_='PropertyCardWrapper__StyledPriceLine')
            for p in price_tags:
                price = p.get_text()
                if '+' in price:
                    self.prices.append(price.split('+')[0].strip())
                else:
                    self.prices.append(price.split('/')[0].strip())

            address_tags = soup.find_all(name='img', class_='Image-c11n-8-84-listing')
            self.addresses = [address.get('alt') for address in address_tags if address.get('alt')]

        except requests.RequestException as e:
            print(f"Error fetching data: {e}")
