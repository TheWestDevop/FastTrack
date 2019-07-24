from django.shortcuts import render
import  requests
import json


# Create your views here.
def live(request):
    
    r = requests.get("https://soccer-livescore.p.rapidapi.com/v1/global/getsoccerscorelive",
       headers={
       "X-RapidAPI-Host": "soccer-livescore.p.rapidapi.com",
       "X-RapidAPI-Key": "9a52a59decmshc3aa7ccd2e2c709p196d87jsn8b2857866d6b"
     }
     )
    lives = r.json()

    return render(request, 'live.html', {'lives':lives})
