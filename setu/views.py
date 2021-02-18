from django.shortcuts import render


# Create your views here.
def setsetu(request):
    print(request)
    return render(request, "setu.html", {
        "setu": "setu_database/かにビーム/DzJ3-03VYAAnK54.jpg"
    })
