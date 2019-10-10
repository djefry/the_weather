import requests
from django.shortcuts import render
from .models import Cities

# Create your views here.


def home(request):
    template_name = "weather/weather.html"
    weathers = []
    if (request.method == 'POST'):
        data = request.POST.copy()
        if(data.get('city')):
            city = data.get('city')
            url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=cd3ed82a0b834e245635bb3bd3c38ae4'
            data = requests.get(url.format(city)).json()
    else:
        objects = Cities.objects.all()
        for object in objects:
            city = object.name
            url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=cd3ed82a0b834e245635bb3bd3c38ae4'
            data = requests.get(url.format(city)).json()
            weather = {
                "city": city,
                "temp": round(data["main"]["temp"]-273, 1),
                "description": data['weather'][0]['description'],
                "icon": data['weather'][0]['icon'],
            }
            weathers.append(weather)
        context = {'weathers': weathers}
        return render(request, template_name, context)
    weather = [{
        "city": city,
        "temp": round(data["main"]["temp"]-273, 1),
        "description": data['weather'][0]['description'],
        "icon": data['weather'][0]['icon'],
    }, ]
    context = {'weathers': weather}
    return render(request, template_name, context)
