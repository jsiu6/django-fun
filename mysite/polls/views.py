from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to my website. I hope my code helped you!")