from django.http import JsonResponse
from django.shortcuts import render
from .models import Movie,Guest,Reservation

 # Create your views here.
# Without rest and no model query :
def no_rest_no_model(request):

    guests = [
        {
            'id':1,
            'name':'mustafa',
        }
        ,
        {
            'id':2,
            'name':'ali',
        }
    ]
    return JsonResponse(guests,safe=False)

#without Rest and using Model query :
def no_rest_from_model(request):
    data = Guest.objects.all()
    response={
        'guests':list(data.values('name','mobile'))
    }
    return JsonResponse(response,safe=False)