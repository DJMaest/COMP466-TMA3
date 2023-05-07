from django.shortcuts import render
# import socket    

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def handleVisit(request, ip):
        # Cookie logic
    visitCount = request.COOKIES.get('count')
    if visitCount is None:
        visitCount = 1
        response = render(request, 'part1/main.html', {"visitCount": visitCount, "clientIp": ip})
    else:
        visitCount = int(visitCount)
        visitCount += 1
        response = render(request, 'part1/main.html', {"visitCount": visitCount, "clientIp": ip})
    response.set_cookie('count', visitCount, max_age=None)
    return response
# Create your views here.
def index(request):
    ip = get_client_ip(request)

    response = handleVisit(request, ip)
    return response


