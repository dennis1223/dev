from django.http import HttpResponse


def index(request):
    return HttpResponse("CONGRATULATIONS!!!")

def beam(request):
    return HttpResponse("Beam. CONGRATULATIONS!!!")