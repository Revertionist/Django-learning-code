from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'this is a trial'},
    {'id': 2, 'name': 'first few lines of django'},
]


def home(request):
    return render(request, "index.html")

def room(request):
    return render(request, "index.html", {'rooms': rooms})