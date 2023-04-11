from django.shortcuts import render
import json
import urllib.request
import urllib.error
from decouple import config

# Create your views here.


def index(request):
    city = ''
    data = {}
    error_message = ''
    if request.method == 'POST':
        city = request.POST['city']
        try:
            response = urllib.request.urlopen(
                'https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+config('WEATHER_API_KEY'))
            print(response)
            # use json.load to convert json string to python dictionary.
            original_data = json.load(response)
            print(type(original_data))  # <class 'dict'>
            data = {
                'country_code': str(original_data['sys']['country']),
                'coordinate': str(original_data['coord']['lon']) + ' ' + str(original_data['coord']['lat']),
                'temp': str(original_data['main']['temp']) + 'k',
                'pressure': str(original_data['main']['pressure']),
                'humidity': str(original_data['main']['humidity']),
            }
        except urllib.error.HTTPError as error:
            error_message = error
    context = {
        'city': city,
        'data': data,
        'error_message': error_message,
    }
    return render(request, 'index.html', context)
