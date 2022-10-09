import requests
from datetime import date, datetime
from django.shortcuts import render

# Create your views here.


def home(request):
    if request.method == "GET":
        return render(request,'home.html')

    if request.method == "POST":
        username=request.POST.get('username','default')
        today = date.today()
        week = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']
        d2 = today.strftime("%B %d, %Y")
        d2 = d2.split()
        place = username

        try:
            url = f'https://api.openweathermap.org/data/2.5/weather?q={place}&units=metric&appid=858f54c9786e8dab5e2306b06f55df26'

            data = requests.get(url)
            data = data.json()
            p = {
                'name': data['name'],
                'country': data['sys']['country'],
                'weather': data['weather'][0]['main'],
                'temprature': round(data['main']['temp']),
                'month': d2[0],
                'year': d2[2],
                'date': str(d2[1]).replace(',', ''),
                'day': week[datetime.today().isoweekday()-1],
                'icon':data['weather'][0]['icon']

            }

            return render(request, 'result.html', p)
        except:
            return render(request, 'noresult.html', {'name':username})
