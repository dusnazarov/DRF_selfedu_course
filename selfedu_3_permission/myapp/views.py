
# 1) /////////////////////////////////
# from .models import *
# from rest_framework import generics
# from .serializers import WomenSerializer
# from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAdminUser


# class WomenAPIListCreate(generics.ListCreateAPIView):
#     queryset=Women.objects.all()
#     serializer_class=WomenSerializer
#     permission_classes=(IsAuthenticatedOrReadOnly, )

# class WomenAPIRetirieveUpdate(generics.RetrieveUpdateAPIView):
#     queryset=Women.objects.all()
#     serializer_class=WomenSerializer
#     permission_classes=(IsAdminUser, )


# class WomenAPIRetrieveDestroy(generics.RetrieveDestroyAPIView):
#     queryset=Women.objects.all()
#     serializer_class=WomenSerializer
#     permission_classes=(IsAdminUser, )
    
    

# 2) /////////////////////////////////
from .models import *
from rest_framework import generics
from .serializers import WomenSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAdminUser
from .permissions import IsAdminOrReadOnly,IsOwnerOrReadOnly

class WomenAPIListCreate(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class WomenAPIRetirieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class WomenAPIRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly, )


