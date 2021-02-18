from django.shortcuts import render,HttpResponse
import random
from setu import pics


# Create your views here.
def setsetu(request):
    # print(request)

    return render(request, "setu.html", {
        # "setu": "setu_database/かにビーム/DzJ3-03VYAAnK54.jpg"
        "setu": random.choice(pics)
    })

