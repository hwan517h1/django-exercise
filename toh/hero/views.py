from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello, wrold!')

def hero_id(request, hero_id):
    return HttpResponse('Your id is %d' %hero_id)

def hero_name(request, name):
    return HttpResponse('Your name is %s' %name)

