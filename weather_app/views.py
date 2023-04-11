from django.shortcuts import render
import json
import urllib.request

# Create your views here.


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        response = urllib.request.urlopen(
            'https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=30d37d80cfdaf0940fe4bc711dfa8bbd')
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
    else:
        city = ''
        data = {}
    context = {
        'city': city,
        'data': data
    }
    return render(request, 'index.html', context)
