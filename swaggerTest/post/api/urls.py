from django.urls import path, include
from rest_framework.routers import SimpleRouter

from post.api import viewset, views

router = SimpleRouter()
router.register(r'posts', viewset.PostViewset, basename='post')
router.register(r'comments', viewset.CommentViewset, basename='comment')

urlpatterns = [
    path('plag/', views.PingView.as_view(), name='ping'),

] + router.get_urls()