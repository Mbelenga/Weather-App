from django.shortcuts import render

import requests
from django.shortcuts import render

def index(request):
    weather_data = {}
    
    if 'city' in request.GET:
        city = request.GET['city']
        api_key =
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon'],
            }
        else:
            weather_data = {'error': 'City not found'}

    return render(request, 'weather_app/index.html', {'weather_data': weather_data})
def home_page(request):
    return render(request, 'base.html')