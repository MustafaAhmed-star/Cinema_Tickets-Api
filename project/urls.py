
from django.contrib import admin
from django.urls import path
from tickets  import views 
urlpatterns = [
     
    path("admin/", admin.site.urls),
    #1
    path('no-rest-no-model',views.no_rest_no_model),
    #2
    path('no-rest-from-model',views.no_rest_from_model),
    #3
    path('rest/list-create', views.list_create_api)
]
