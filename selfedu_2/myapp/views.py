# 1) //////////////////////////////////////
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Women
# from .serializers import WomenSerializer


# class WomenAPIView(APIView):    
#     def get(self, request):
#         w = Women.objects.all() 
#         return Response({'posts':WomenSerializer(w, many=True).data })
    
#     def post(self,request):
#         post_new = Women.objects.create(
#             title = request.data['title'],
#             content = request.data['content'],
#             cat_id = request.data['cat_id']
#         )        
#         return Response({'post':WomenSerializer(post_new).data})


# 2) ////////////////////////////////////////////////
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from .models import Women
# from .serializers import WomenSerializer


# class WomenAPIView(APIView):
#     def get(self,request):
#         w = Women.objects.all()
#         return Response({'posts':WomenSerializer(w, many=True).data})

#     def post(self,request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
        
#         return Response({'post':serializer.data})
    
#     def put(self,request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({'error':'Method PUT not allowed'})

#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({'error':'Object does not exists'})

#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post':serializer.data})
    
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({'error':'Method DELETE not allowed'})

#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({'error':'Object does not exists'})
        
#         instance.delete()  
#         return Response({'post':'delete post '+str(pk)})


# 3) ////////////////////////////////////////////////
# from rest_framework import generics
# from .models import Women
# from .serializers import WomenModelSerializer

# class WomenAPIListCreate(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenModelSerializer
    
# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenModelSerializer

# class WomenAPIDetailDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenModelSerializer
  

# 4), 5)  ////////////////////////////////////////////////////
# from rest_framework import viewsets
# from .models import Women
# from .serializers import WomenModelSerializer

# class WomenViewSet(viewsets.ModelViewSet):
#     queryset = Women.objects.all()
#     serializer_class = WomenModelSerializer


# 6) ////////////////////////////////////////////////
# from .models import Women
# from rest_framework import mixins
# from rest_framework.viewsets import GenericViewSet
# from .serializers import WomenModelSerializer 

# class WomenViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.ListModelMixin,
#                    mixins.DestroyModelMixin,
#                    GenericViewSet
#                    ):

#     queryset=Women.objects.all()
#     serializer_class=WomenModelSerializer


# 7) ////////////////////////////////////////////////
# from .models import Women
# from rest_framework import viewsets
# from .serializers import WomenModelSerializer 

# class WomenViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Women.objects.all()
#     serializer_class = WomenModelSerializer


# 8) ////////////////////////////////////////////////
# from .models import Women, Category
# from rest_framework import viewsets
# from rest_framework.decorators import action
# from .serializers import WomenModelSerializer 
# from rest_framework.response import Response

# class WomenViewSet(viewsets.ModelViewSet):
#     queryset = Women.objects.all()
#     serializer_class = WomenModelSerializer
   

#     @action(methods = ['get'], detail=False)
#     def category(self, request ):
#         cats = Category.objects.all()
#         return Response({'cats':[c.name for c in cats]})


# 9) ////////////////////////////////////////////////
# from .models import Women, Category
# from rest_framework import viewsets
# from rest_framework.decorators import action
# from .serializers import WomenModelSerializer 
# from rest_framework.response import Response

# class WomenViewSet(viewsets.ModelViewSet):
#     queryset = Women.objects.all()
#     serializer_class = WomenModelSerializer
        
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats':cats.name})

# 10)///////////////////////////////////////////////////
from .models import Women, Category
from rest_framework import viewsets
from rest_framework.decorators import action
from .serializers import WomenModelSerializer 
from rest_framework.response import Response

class WomenViewSet(viewsets.ModelViewSet):    
    serializer_class = WomenModelSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Women.objects.all()[:3]
        return Women.objects.filter(pk=pk)
    
    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats':cats.name})

