from django.http import HttpResponse
from .models import City

def index(request):
    mydata = City.objects.all().values()
    print(mydata)
    return HttpResponse(mydata)
