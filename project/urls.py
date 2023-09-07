
from django.contrib import admin
from django.urls import include, path
from tickets  import views 
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('guests',views.ViewSetGuest)
router.register('movies',views.ViewSetMovie)
router.register('reservation',views.ViewSetReservation)
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
    #5 CBV GET + POST from DRF
    path('rest/cbv/api',views.ListCreateApi.as_view()),
    #6 CBV GET PUT DELETE from DRF
    path('rest/cbv/api/<int:pk>/',views.RetriveUpdateDeleteApi.as_view()),
    #7 Mixins GET  POST 
    path('rest/mixins/create/',views.MixinsListCreate.as_view()),
    #8 Mixins Retrieve PUT DELETE(Destroy)
    path('rest/mixins/create/<int:pk>/',views.MixinsRetrieveUpdateDelete.as_view()),
    # 9 Generics GET POST
    path('rest/generics/create/',views.ListCreateGenericApi.as_view()),
    #10 Generics GET PUT DELETE

    path('rest/generics/create/<int:pk>/',views.RetrieveUpdateDeleteApiGenerics.as_view()),
    #11 Viewsets For all CRUD opperations (all models)
    path('rest/viewsets/', include(router.urls)),
    #12 search fbv
    path('rest/api/search',views.find_movie),
    #13 Reservation create
    path('res/dev/',views.create_reversation),
]
