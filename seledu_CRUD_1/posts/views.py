from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework import status
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# # ///////// CRUD Class Based View (APIView) //////////////////////////////////////
class PostListCreateUpdateDeleteAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            posts = Post.objects.all()
            serializer = PostSerializer(instance=posts, many=True)

            response = {
                "message":"List Posts",
                "data":serializer.data
                
            }
            return Response(data=response, status=status.HTTP_200_OK )
        if pk:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(instance=post, many=False)

            response = {
                "message":"Post Detail",
                "data":serializer.data
            }
            return Response(data=response, status=status.HTTP_200_OK)    
    
    def post(self, request):
        data = request.data
        serializer = PostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message":"Post Created",
                "data":serializer.data
            }        
                
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        
        if not pk:
            response = {"message":"error':'Method PUT not allowed" }
                       
            return Response(data=response, status=status.HTTP_403_FORBIDDEN)

        try:
            post = Post.objects.get(pk=pk)
        except:
            response = { "message":"error':'Post does not exists" }
               
           
            return Response(data=response, status=status.HTTP_204_NO_CONTENT)
        
        data = request.data
        
        serializer = PostSerializer(instance=post, data=data)        
        if serializer.is_valid():
            serializer.save()

            response = {
                "message":"Post Updated successfully",
                "data":serializer.data
            }
            return Response(data=response, status=status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            response = {"message":"error':'Method DELETE not allowed"}
            return Response(data=response, status=status.HTTP_403_FORBIDDEN)

        try:
            post = Post.objects.get(pk=pk)
        except:
            response = {"message":"error':'Post does not exists"}
            return Response(data=response)
        
        post.delete()
        response = {"message":" post " + str(pk) +  " deleted "}  
        return Response(data=response, status=status.HTTP_204_NO_CONTENT)



# # //////////////////// CRUD Class Based View (generics )   ////////////////////////////
class PostListCreateAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
       
  

# # ///////////////// CRUD Class Based View ( ModelViewset)     //////////////////////////////////
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# # ///////////////// CRUD Class Based View ( ModelViewset)     //////////////////////////////////
class PostCRUDViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
