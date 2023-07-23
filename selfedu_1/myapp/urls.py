from django.urls import path,  include
from .views import WomenAPIListCreate, WomenAPIUpdate, WomenAPIDetailDeleteView, WomenViewSet, WomenAPIView
from rest_framework import routers



# 1) ///////////////////////////////////////////////
urlpatterns=[
    path('list/',WomenAPIView.as_view()),
    path('create/',WomenAPIView.as_view()),
    path('<int:pk>/update/', WomenAPIView.as_view()),
    path('<int:pk>/delete/', WomenAPIView.as_view()),

]

# 2) ///////////////////////////////////////////////
# urlpatterns=[
#     path('list/', WomenAPIListCreate.as_view()),
#     path('create/', WomenAPIListCreate.as_view()),    
#     path('<int:pk>/detail/', WomenAPIDetailDeleteView.as_view()),
#     path('<int:pk>/delete/', WomenAPIDetailDeleteView.as_view()),   
#     path('<int:pk>/update/', WomenAPIUpdate.as_view()),
    
# ]


# 3) /////////////////////////////////////////////////
# urlpatterns = [
#     path('list/', WomenViewSet.as_view({'get':'list'})),
#     path('<int:pk>/detail/', WomenViewSet.as_view({'get':'retrieve'})),
#     path('create/', WomenViewSet.as_view({'post':'create'})),   
#     path('<int:pk>/update/', WomenViewSet.as_view({'put':'update'})),
#     path('<int:pk>/delete/', WomenViewSet.as_view({'delete':'destroy'})),    
    
# ]

# 4) /////////////////////////////////////////////////

# router = routers.SimpleRouter()  
# router.register(r'women', WomenViewSet)

# # router = routers.DefaultRouter()
# # router.register(r'women', WomenViewSet)

# # print(router.urls)

# urlpatterns = [
#     path('v1/', include(router.urls)), # http://127.0.0.1:8000/api/v1/women/
# ] 

# 5)  /////////////////////////////////////////////////

# router = routers.DefaultRouter()
# router.register(r'women', WomenViewSet)

# urlpatterns = [
#     path('v1/', include(router.urls)), # http://127.0.0.1:8000/api/v1/women/category/
# ] 

# 6)  /////////////////////////////////////////////////

# router = routers.DefaultRouter()
# router.register(r'women', WomenViewSet)

# urlpatterns = [
#     path('v1/', include(router.urls)), # http://127.0.0.1:8000/api/v1/women/pk/category/
# ] 


# 7)  /////////////////////////////////////////////////

# router = routers.DefaultRouter()
# router.register(r'women', WomenViewSet, basename='women')

# urlpatterns = [
#     path('v1/', include(router.urls)), # http://127.0.0.1:8000/api/v1/women/pk/category/
# ] 



