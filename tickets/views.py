from django.http import JsonResponse
from django.shortcuts import render
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