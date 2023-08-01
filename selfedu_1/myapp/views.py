from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Women, Category
from .serializers import WomenSerializer
from rest_framework import generics, viewsets
from rest_framework.decorators import action


# 1) ////////////////////////////////////////////////
class WomenAPIView(APIView):
    def get(self, request, *args, **kwargs):

        pk = kwargs.get('pk', None)

        if not pk:
            queryset = Women.objects.all()
            serializer = WomenSerializer(queryset, many=True)
            return Response(serializer.data, )
        if pk:
            obj = Women.objects.get(pk=pk)
            serializer = WomenSerializer(obj, many=False)
            return Response(serializer.data)    
    
    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()        
        return Response(serializer.data)
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        
        if not pk:
            return Response({'error':'Method PUT not allowed'})

        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({'error':'Object does not exists'})

        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({'error':'Method DELETE not allowed'})

        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({'error':'Object does not exists'})
        
        instance.delete()  
        return Response({'post':'delete post ' + str(pk)})


# # 2) ////////////////////////////////////////////////
class WomenAPIListCreate(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    
class WomenAPIUpdate(generics.UpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

class WomenAPIDetailDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
  

# #3), 4)  ////////////////////////////////////////////////////

class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

# #5) ////////////////////////////////////////////////

class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
   

    @action(methods = ['get'], detail=False)
    def category(self, request ):
        cats = Category.objects.all()
        return Response({'cats':[c.name for c in cats]})


# #6) ////////////////////////////////////////////////
class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
        
    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats':cats.name})

# # 7)///////////////////////////////////////////////////

class WomenViewSet(viewsets.ModelViewSet):    
    serializer_class = WomenSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Women.objects.all()[:3]
        return Women.objects.filter(pk=pk)
    
    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats':cats.name})

