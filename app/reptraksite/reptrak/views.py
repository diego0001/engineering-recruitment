from django.http import JsonResponse
from reptrak.models import Reptrak


def index(request):
    response = []
    for object in Reptrak.objects.all():
        object_id = object.id
        if object_id % 3 == 0 and object_id % 5 == 0:
            response.append('reptrak')
        elif object_id % 3 == 0:
            response.append('rep')
        elif object_id % 5 == 0:
            response.append('trak')
        else:
            response.append(object_id)
    return JsonResponse(response, safe=False)
