from django.shortcuts import render
from django.http import HttpResponse
import json
import re
# Create your views here.

laptops = [
    {
        "model": "Model 1",
        "RAM": {"base": "8GB", "upgrades": [{"size": "16GB", "premium": "100"}]},
        "storage": {"base": "256GB", "upgrades": [{"size": "512GB", "premium": "200"}]},
        "CPU": {"base": "Intel Core i5", "upgrades": [{"type": "Intel Core i7", "premium": "200"}]},
        "display":"13\"",
        "OS":"Ubuntu",
        "soundcard":"yes",
        "price":"999"
    },
    {
        "model": "Model 2",
        "RAM": {"base": "16GB", "upgrades": [{"size": "32GB", "premium": "200"}, {"size": "64GB", "premium": "400"}]},
        "storage": {"base": "512GB", "upgrades": [{"size": "1TB", "premium": "400"}]},
        "CPU": {"base": "Intel Core i7", "upgrades": [{"type": "Intel Core i9", "premium": "200"}]},
        "display": "13\"",
        "OS": "Ubuntu",
        "soundcard": "yes",
        "price": "1399"
    },
    {
        "model": "Model 3",
        "RAM": {"base": "16GB", "upgrades": [{"size": "32GB", "premium": "200"}, {"size": "64GB", "premium": "400"}, {"size": "128GB", "premium": "800"}]},
        "storage": {"base": "512GB", "upgrades": [{"size": "1TB", "premium": "400"}, {"size": "2TB", "premium": "800"}]},
        "CPU": {"base": "Intel Core i7", "upgrades": [{"type": "Intel Core i9", "premium": "200"}, {"type": "Intel Xeon", "premium": "400"}]},
        "display": "16\"",
        "OS": "Ubuntu",
        "soundcard": "yes",
        "price": "1699"
    },

]

desktops = [
    {
        "model": "Model 1",
        "RAM": {"base": "8GB", "upgrades": [{"size": "16GB", "premium": "100"}]},
        "storage": {"base": "256GB", "upgrades": [{"size": "512GB", "premium": "200"}]},
        "CPU": {"base": "Intel Core i5", "upgrades": [{"type": "Intel Core i7", "premium": "200"}]},
        "GPU": {"base": "RTX 1650", "upgrades": [{"type": "RTX 2070", "premium": "400"}]},
        "display":"24\"",
        "OS":"Ubuntu",
        "soundcard":"yes",
        "price":"1399"
    },
    {
        "model": "Model 2",
        "RAM": {"base": "16GB", "upgrades": [{"size": "32GB", "premium": "200"}, {"size": "64GB", "premium": "400"}]},
        "storage": {"base": "512GB", "upgrades": [{"size": "1TB", "premium": "400"}]},
        "CPU": {"base": "Intel Core i7", "upgrades": [{"type": "Intel Core i9", "premium": "200"}]},
        "GPU": {"base": "RTX 2070", "upgrades": [{"type": "RTX 2080", "premium": "400"}]},
        "display": "24\"",
        "OS": "Ubuntu",
        "soundcard": "yes",
        "price": "1699"
    },
    {
        "model": "Model 3",
        "RAM": {"base": "16GB", "upgrades": [{"size": "32GB", "premium": "200"}, {"size": "64GB", "premium": "400"}, {"size": "128GB", "premium": "800"}]},
        "storage": {"base": "512GB", "upgrades": [{"size": "1TB", "premium": "400"}, {"size": "2TB", "premium": "800"}]},
        "CPU": {"base": "Intel Core i7", "upgrades": [{"type": "Intel Core i9", "premium": "200"}, {"type": "Intel Xeon", "premium": "400"}]},
        "GPU": {"base": "RTX 2070", "upgrades": [{"type": "RTX 2080", "premium": "400"},{"type": "RTX 3070", "premium": "600"},{"type": "RTX 3080", "premium": "800"}]},
        "display": "27\"",
        "OS": "Ubuntu",
        "soundcard": "yes",
        "price": "1999"
    },

]


def index(request):
    return render(request, "part3/main.html")


def laptop(request):

    return render(request, "part3/laptop.html", {"laptops": laptops})

def laptopConfig(request, pk):
    laptop = next(item for item in laptops if item["model"] == pk)
    return render(request, "part3/laptopConfig.html", {"laptop": laptop})

def bag(request):
    bagItemsCookie = request.COOKIES.get("bagItems")
    
    if bagItemsCookie is not None:
        items = json.loads(request.COOKIES.get("bagItems").replace("%22","\"").replace("%2C",",").replace("%20"," "))
        total = 0
        for item in items:
            total += item["price"]
        return render(request,  "part3/bag.html", {"items": items, "total":total})
    else:
        return render(request,  "part3/bag.html", {"items":[]})

def order(request):
    return render(request, "part3/order.html")

def desktop(request):
    return render(request, "part3/desktop.html", {"desktops": desktops})

def desktopConfig(request, pk):
    desktop = next(item for item in desktops if item["model"] == pk)
    return render(request, "part3/desktopConfig.html", {"desktop": desktop})

def contact(request):

    return render(request, "part3/contact.html")

def search(request):
    results =[]
    if request.GET:
        model = request.GET.get("query")
        print(model)
        if model=="":
            return render(request, "part3/search.html", {"results": results})
        reg = re.compile(model, re.IGNORECASE)
        for l in laptops:
            if re.match(reg, l["model"]):
                results.append(l)
        for d in desktops:
            if re.match(reg, d["model"]):
                results.append(d)

    return render(request, "part3/search.html", {"results": results})

def feedback(request):
    return render(request, "part3/feedback.html")


