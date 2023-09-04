
from django.contrib import admin
from django.urls import path
from tickets  import views 
urlpatterns = [
    path("admin/", admin.site.urls),
    path('no-rest-no-model',views.no_rest_no_model)
]
