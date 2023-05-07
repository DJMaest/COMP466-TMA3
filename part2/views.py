from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
def index(request):
    images = json.load(open("shared/images/part2/imageList.json"))
    return render(request, "part2/main.html", images)

def laptop(request):
    return HttpResponse("Laptop")