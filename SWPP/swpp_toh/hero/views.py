from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from .models import Hero
import json
from json.decoder import JSONDecodeError


@csrf_exempt
def hero_list(request):
    if request.method == 'GET':
        hero_all_list = [hero for hero in Hero.objects.all().values()]
        # .value()는 Python과 Javascript가 서로 인식할 수 있도록 common data type(json)로 바꾸는 것(이 방식을 serialization이라고 함)
        return JsonResponse(hero_all_list, safe=False)
        # python에서 제공하는 JsonResponse는 python의 dictionary를 json으로 변환함
    elif request.method == 'POST':
        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
            # json 형식으로 보냈을 것이라고 여기고 assume하는 것
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()
        hero = Hero(name=hero_name)
        hero.save()
        response_dict = {
            'id': hero.id,
            'name': hero.name,
        }
        return JsonResponse(response_dict, status=201)  # created
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


@csrf_exempt
def hero_detail(request, hero_id):
    if request.method == 'GET':
        try:
            hero = Hero.objects.get(id=hero_id)
        except Hero.DoesNotExist:
            return HttpResponseNotFound()
        response_dict = {
            'id': hero.id,
            'name': hero.name,
        }
        return JsonResponse(response_dict)
    elif request.method == 'PUT':
        try:
            hero = Hero.objects.get(id=hero_id)
        except Hero.DoesNotExist:
            return HttpResponseNotFound()

        try:
            body = request.body.decode()
            hero_name = json.loads(body)['name']
        except (KeyError, JSONDecodeError) as e:
            return HttpResponseBadRequest()

        hero.name = hero_name
        hero.save()
        return HttpResponse(status=204)
    elif request.method == 'DELETE':
        try:
            hero = Hero.objects.get(id=hero_id)
        except Hero.DoesNotExist:
            return HttpResponseNotFound()

        hero.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponseNotAllowed(['GET', 'PUT', 'DELETE'])
