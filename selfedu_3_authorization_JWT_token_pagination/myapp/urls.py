

# 1), 2) ////////////////////////////////
from django.urls import path
from .views import *

urlpatterns=[    
    path('list/', WomenAPIListCreate.as_view()),
    path('<int:pk>/detail/', WomenAPIRetirieveUpdate.as_view()),
    path('create/', WomenAPIListCreate.as_view()),   
    path('<int:pk>/update/', WomenAPIRetirieveUpdate.as_view()),
    path('<int:pk>/delete/', WomenAPIRetrieveDestroy.as_view()),
    
]


