"""Every views in Rest called endpoint"""
from django.http.response import JsonResponse  
from django.shortcuts import render
from .models import Movie,Guest,Reservation
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import  generics , mixins
'''
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
    return JsonResponse(response )
'''
#Function based view 
#GET POST
@api_view(['GET','POST'])
def list_create_api(request):
    #GET
    if request.method == 'GET':
        gusets= Guest.objects.all()
        serializer = GuestSerialzers(gusets,many = True)
        return Response(serializer.data)
    #post
    elif request.method == 'POST':
        serializer  = GuestSerialzers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#FBV GET PUT DELETE
@api_view(['GET','PUT','DELETE'])
def detail_update_delete_api(request,pk):
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #GET
    if request.method == 'GET':
        serializer = GuestSerialzers(guest)
        return Response(serializer.data)
    # PUT
    elif request.method == 'PUT':
        serializer = GuestSerialzers(guest,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    #DELETE 
    if request.method == 'DELETE':
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#CBV GET POST
class ListCreateApi(APIView):
    #GET
    def get(self,request):
        guests = Guest.objects.all()
        serializer = GuestSerialzers(guests,many = True)
        return Response(serializer.data)
    #POST
    def post(self,request):
        serializer = GuestSerialzers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    

# CBV GET PUT DELETE
class RetriveUpdateDeleteApi(APIView):
    def get_object(self,pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            raise Http404
    #GET--->pk
    def get (self,request,pk):
        guest = self.get_object(pk)
        serializer = GuestSerialzers(guest)
        return Response(serializer.data)
    #PUT
    def put(self,request,pk):
        guest = self.get_object(pk)
        serializer = GuestSerialzers(guest,data=request.data )
        if serializer.is_valid(self):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    #DELETE
    def delete(self,request,pk):
        guest= self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#Mixing-->list,Create
class MixinsListCreate(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerialzers
    #GET 
    def get(self,request):
        return self.list(request)
    #POST 
    def post(self,request):
        return self.create(request)
    
class MixinsRetrieveUpdateDelete(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerialzers
    def get(self,request,pk):
        return self.retrieve(request)
    def put(self,request,pk):
        return self.update(request)
    def delete(self,request,pk):
        return self.destroy(request)

###Generics###
# GET POST
class ListCreateGenericApi(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerialzers
# GET PUT DELETE
class RetrieveUpdateDeleteApiGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerialzers