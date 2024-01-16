from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from . models import weather
import datetime
import requests

time= datetime.datetime.now().strftime("%H-%M-%S")
variable=time
def weathert(request):
        if request.method == 'POST':
                city=request.POST.get('cityname')

                url=f'http://api.openweathermap.org/data/2.5/weather?q={city},&appid=1dbbf8cb7450cde089e9891aae0318a2'
                data=requests.get(url).json()
                if data['cod'] == 200:
                        payload ={'city': data['name'],
                                  'weather': data['weather'][0]['main'],
                                  'icon' : data['weather'][0]['icon'],
                                  'pressure' : data['main']['pressure'],
                                  'kelvin_temperature': data['main']['temp'],
                                  'humidity': data['main']['humidity'],
                                  'celsius_temperature': data['main']['temp'] - 273,
                        }
                        context={'data':payload}
                        weather_data = weather(
                            city=payload['city'],
                            weather=payload['weather'],
                            pressure=payload['pressure'],
                            kelvin_temperature=payload['kelvin_temperature'],
                            humidity=payload['humidity'],
                            celsius_temperature=payload['celsius_temperature'])
                        weather_data.save()
                      
                        messages.success(request,""+city+"added successfully")
                        
                        return render(request,"weather.html",context)
                else:
                     messages.error(request,""+city+" does not exist")
        return render(request,"weather.html")     

"""def add():
        jas=weather(city=['name'],weather= data['weather'][0]['main'],
                    pressure=data['main']['pressure'],kelvin_temperature= data['main']['temp'],
                    humidity= data['main']['humidity'],
                    celsius_temperature= data['main']['temp'] - 273,)

        jas.save()
        messages.success(request,""+city+"added successfully")
        return render(request,"weather.html",context)"""
        
        







"""if request.method == 'POST':
                        form=city(request.POST)
                        if form.is_valid():
                                ncity=form.cleaned_data['cityname']#text box la kudukura values ah ncity la store pandrom
                                ccity=city.objects.filter(cityname=ncity).count()
                                if ccity==0:
                                        res=request.get(url.format(ncity)).json()
                                        if res['cod']==200:
                                                form.save()
                                                messages.success(request,""+ncity+"added successfully")
                                        else:
                                                messages.error(request,""+ncity+"city does not exist")
                        else:
                                messages.error(request,""+ncity+"already exists") 
                p=city()
                cities=city.objects.all()
                return render(request,"weather.html",{"cit1ies":city})"""


        