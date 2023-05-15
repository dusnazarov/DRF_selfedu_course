# 1,2 va 3 larni bitta url da tekshirilgan
from django.urls import path
from .views import WomenAPIView

urlpatterns=[
    path('api/',WomenAPIView.as_view())
]
