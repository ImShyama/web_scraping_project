from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


def Myview(request):
    weather_data = None

    if 'city' in request.GET:
        city = request.GET.get('city')
        city = city.replace(' ', '+')
        
        # url, Header and Page material
        url = f'https://www.google.com/search?ei=b2PoXr3dO9i5rQHeuY6QBA&q=weather+{city}'
        headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
                    "accept-Language": 'en,en-gb;q=0.5'}
        page = requests.get(url, headers=headers)

        # Content all the html in the given url
        soup = BeautifulSoup(page.content, 'html.parser')
        
        weather_data = dict()
        weather_data['title'] = soup.find(id='wob_loc').getText().strip()
        weather_data['day_date'] = soup.find(id = 'wob_dts').getText().strip()
        weather_data['temp'] = soup.find(id = 'wob_tm').getText().strip() + '° C'
        weather_data['status'] = soup.find(id = 'wob_dc').getText().strip()


    return render(request, 'index.html', {'weather':weather_data})
