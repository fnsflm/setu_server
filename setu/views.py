from django.shortcuts import render
import random
from setu import pics
from urllib.parse import quote


# Create your views here.
def setsetu(request):
    # print(request)

    return render(request, "setu.html", {
        # "setu": "setu_database/かにビーム/DzJ3-03VYAAnK54.jpg"
        "setu": quote(random.choice(pics), 'utf-8')
    })
