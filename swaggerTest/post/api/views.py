from rest_framework import generics
from api.models import Post, Comment
from api.serializers



class PingView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = WomenSerializer


