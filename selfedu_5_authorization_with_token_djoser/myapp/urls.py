

# 1), 2) ////////////////////////////////
from django.urls import path, include
from .views import *

urlpatterns=[    
    path('list/', WomenAPIListCreate.as_view()),
    path('list/detail/<int:pk>/', WomenAPIRetirieveUpdate.as_view()),
    path('list/create/', WomenAPIListCreate.as_view()),   
    path('list/update/<int:pk>/', WomenAPIRetirieveUpdate.as_view()),
    path('list/delete/<int:pk>/', WomenAPIRetrieveDestroy.as_view()),
    
]


