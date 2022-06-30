
import bs4, requests
def weat():
    # Set headers
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0", "Accept-Language":"pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3"}
    # Link to accuweather in the right location.
    link = 'https://www.accuweather.com/pt/br/santa-m%C3%B4nica/2728202/weather-forecast/2728202'
    # Get page and soup it.
    page = requests.get(link, headers=headers)
    page.raise_for_status()
    a = bs4.BeautifulSoup(page.content, 'html.parser') # soup
    # Set Selectors to temperature, weather and quality of the air
    # Save the information
    sele_tempera = "body > div > div.two-column-page-content > div.page-column-1 > div.content-module > a.cur-con-weather-card.card-module.non-ad.content-module.lbar-panel > div.cur-con-weather-card__body > div:nth-child(1) > div > div > div.temp"
    temperatura = a.select(sele_tempera)[0].text
    sele_tempo = "body > div > div.two-column-page-content > div.page-column-1 > div.content-module > a.cur-con-weather-card.card-module.non-ad.content-module.lbar-panel > div.spaced-content > span.phrase"
    tempo = a.select(sele_tempo)[0].text
    sele_quali = 'div.detail:nth-child(2) > span:nth-child(2)'
    quali = a.select(sele_quali)[0].text
    # Define the bg color based on quality of the air
    color = def_color(quali)
    # Return a tuple with all information
    return temperatura, tempo, quali, color


def def_color(quali):
    # Define the bg color based on quality of the air, like in accuweather
    if quali == 'Excelente':
        color = '#00E39B'
    elif quali == 'Razoável':
        color  = '#FFC300'
    elif quali == 'Ruim':
        color  = '#ff712b'
    elif quali == 'Insalubre':
        color  = '#f62a55'
    elif quali == 'Muito insalubre':
        color  = '#c72eaa'
    elif quali == 'Perigoso':
        color  = '#9930ff'
    else:
        color = 'white'
    return color
