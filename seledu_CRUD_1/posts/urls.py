from django.urls import path,  include
from . import views 
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'posts', views.PostCRUDViewSet)



# #/////////////////////    //////////////////////////
urlpatterns=[
    path('list/', views.PostListCreateUpdateDeleteAPIView.as_view(), name="post-list"),
    path('detail/<int:pk>/', views.PostListCreateUpdateDeleteAPIView.as_view(), name="post-detail"),
    path('create/', views.PostListCreateUpdateDeleteAPIView.as_view(), name="post-create"),
    path('update/<int:pk>/', views.PostListCreateUpdateDeleteAPIView.as_view(), name="post-update"),
    path('delete/<int:pk>/', views.PostListCreateUpdateDeleteAPIView.as_view(), name="post-delete"),


# # ////////////////////  generics   ////////////////////////////
    path('glist/', views.PostListCreateAPIView.as_view(), name="gpost-list"),
    path('gdetail/<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view(), name="gpost-detail"),
    path('gcreate/', views.PostListCreateAPIView.as_view(), name="gpost-create"),
    path('gupdate/<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view(), name="gpost-update"),
    path('gdelete/<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view(), name="gpost-delete"),

# # ////////////////////  ModelViewset   ////////////////////////////    

    path('vlist/', views.PostViewSet.as_view({'get':'list'})),
    path('vdetail/<int:pk>/', views.PostViewSet.as_view({'get':'retrieve'})),
    path('vcreate/', views.PostViewSet.as_view({'post':'create'})),   
    path('vupdate/<int:pk>', views.PostViewSet.as_view({'put':'update'})),
    path('vdelete/<int:pk>', views.PostViewSet.as_view({'delete':'destroy'})),
     
# # ////////////////////  ModelViewset (PostCRUDViewSet)  ////////////////////////////   
    path('v/', include(router.urls)), # http://127.0.0.1:8000/api/v/posts/   
    

]



