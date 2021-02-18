from django.shortcuts import render
import random
from setu import pics
from urllib.parse import quote


# Create your views here.
def setsetu(request):
    test = request.GET.get('test')
    test = test if test else '0'
    seturl = "/" + quote(random.choice(pics), 'utf-8')
    if test != '0':
        seturl = "https://cdn.jsdelivr.net/gh/fnsflm/myPicbed/photo_2021-02-14_18-00-46.jpg"
    return render(request, "setu.html", {
        # "setu": "setu_database/かにビーム/DzJ3-03VYAAnK54.jpg"
        "setu": seturl
    })
