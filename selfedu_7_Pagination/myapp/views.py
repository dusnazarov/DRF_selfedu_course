
# 1) /////////////////////////////////
from .models import *
from rest_framework import generics
from .serializers import WomenSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAdminUser, IsAuthenticated
from .permissions import IsAdminOrReadOnly,IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination


class WonenAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_parm = 'page_size'
    max_page_size = 10000


class WomenAPIListCreate(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer    
    permission_classes = (IsAuthenticated, )
    pagination_class =WonenAPIListPagination
   

    
class WomenAPIRetirieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated, )
  


class WomenAPIRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    # permission_classes = (IsAdminOrReadOnly, )
    permission_classes = (IsAuthenticated, )


