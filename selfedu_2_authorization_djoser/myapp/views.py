
from .models import *
from rest_framework import generics
from .serializers import WomenSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


# 1) /////////////////////////////////
# class WomenAPIListCreate(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#     permission_classes=(IsAuthenticatedOrReadOnly, )

# class WomenAPIRetirieveUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#     permission_classes = (IsAdminUser, )


# class WomenAPIRetrieveDestroy(generics.RetrieveDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#     permission_classes = (IsAdminUser, )    
    

# 2) /////////////////////////////////

class WomenAPIListCreate(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer    
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)

class WomenAPIRetirieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    
class WomenAPIRetirieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated, )
  


class WomenAPIRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer   
    permission_classes = (IsAuthenticated, )


