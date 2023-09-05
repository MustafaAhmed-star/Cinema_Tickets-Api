
from django.contrib import admin
from django.urls import path
from tickets  import views 
urlpatterns = [
     
    path("admin/", admin.site.urls),
    #1
  #  path('no-rest-no-model',views.no_rest_no_model),
    #2
  #  path('no-rest-from-model',views.no_rest_from_model),
    #3 GET  POST  from DRF
    path('rest/api/', views.list_create_api),
    #4 GET PUT DELETE from DRF
    path('rest/api/<int:pk>/', views.detail_update_delete_api),
    #5 CBV GET + POST
    path('rest/cbv/api',views.ListCreateApi.as_view())
]
