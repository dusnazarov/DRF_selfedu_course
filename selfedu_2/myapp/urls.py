
# 1) ///////////////////////////////////////////////
# from django.urls import path
# from .views import WomenAPIView

# urlpatterns=[
#     path('list/',WomenAPIView.as_view()),
#     path('list/create/',WomenAPIView.as_view()),   

# ]


# 2) ///////////////////////////////////////////////
# from django.urls import path
# from .views import WomenAPIView

# urlpatterns=[
#     path('list/',WomenAPIView.as_view()),
#     path('list/create/',WomenAPIView.as_view()),
#     path('list/update/<int:pk>/', WomenAPIView.as_view()),
#     path('list/delete/<int:pk>/', WomenAPIView.as_view()),

# ]

# 3) ///////////////////////////////////////////////
# from django.urls import path
# from .views import WomenAPIListCreate, WomenAPIUpdate, WomenAPIDetailDeleteView

# urlpatterns=[
#     path('list/', WomenAPIListCreate.as_view()),
#     path('list/create/', WomenAPIListCreate.as_view()),    
#     path('list/detail/<int:pk>/', WomenAPIDetailDeleteView.as_view()),
#     path('list/delete/<int:pk>/', WomenAPIDetailDeleteView.as_view()),   
#     path('list/update/<int:pk>/', WomenAPIUpdate.as_view()),
    
# ]


# 4) /////////////////////////////////////////////////
# from django.urls import path
# from .views import WomenViewSet

# urlpatterns = [
#     path('list/', WomenViewSet.as_view({'get':'list'})),
#     path('list/detail/<int:pk>/', WomenViewSet.as_view({'get':'retrieve'})),
#     path('list/create/', WomenViewSet.as_view({'post':'create'})),   
#     path('list/update/<int:pk>/', WomenViewSet.as_view({'put':'update'})),
#     path('list/delete/<int:pk>/', WomenViewSet.as_view({'delete':'destroy'})),
    
    
# ]

# 5), 6), 7) /////////////////////////////////////////////////
# from django.urls import path, include
# from .views import WomenViewSet
# from rest_framework import routers

# router = routers.SimpleRouter()  
# router.register(r'women', WomenViewSet)

# # router = routers.DefaultRouter()
# # router.register(r'women', WomenViewSet)

# # print(router.urls)

# urlpatterns = [
#     path('v1/', include(router.urls)), # http://127.0.0.1:8000/api/v1/women/
# ] 

# 8)  /////////////////////////////////////////////////
# from django.urls import path, include
# from .views import WomenViewSet
# from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'women', WomenViewSet)

# urlpatterns = [
#     path('v1/', include(router.urls)), # http://127.0.0.1:8000/api/v1/women/category/
# ] 

# 9)  /////////////////////////////////////////////////
# from django.urls import path, include
# from .views import WomenViewSet
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'women', WomenViewSet)

# urlpatterns = [
#     path('v1/', include(router.urls)), # http://127.0.0.1:8000/api/v1/women/pk/category/
# ] 


# 10)  /////////////////////////////////////////////////
from django.urls import path, include
from .views import WomenViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'women', WomenViewSet, basename='women')

urlpatterns = [
    path('v1/', include(router.urls)), # http://127.0.0.1:8000/api/v1/women/pk/category/
] 



