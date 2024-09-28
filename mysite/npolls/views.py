from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Nhi's at the polls index.")