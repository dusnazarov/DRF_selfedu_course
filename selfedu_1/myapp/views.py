from rest_framework.views import APIView 
from rest_framework.response import Response
from .models import Women
from django.forms import model_to_dict


# 1)  ////////////////////////////////////////////////////////////////////////////
# get va post requests  larni hosil qilyabmiz bitta class da serializer va model siz

# class WomenAPIView(APIView):
#     def get(self,request):
#         return Response({'title':'get'})

#     def post(self,request):
#         return Response({'title':'post'})

# 2) ///////////////////////////////////////////////////////////////
# get request bilan modeldagi jami qiymatlarini list kurinishida olyabmiz

# class WomenAPIView(APIView):
#     def get(self,request):
#         lst = Women.objects.all().values()
#         # print(lst)
#         return Response({'posts':lst})


# 3) ///////////////////////////////////////////////////////////////////////////
# hozirgacha biz post qilganimizda bazaga malumot qo'shmayotgan edi, endi bazaga ma'lumot qo'shamiz,
#  postman ga {} ichiga yozib malumotlarni qo'shamiz.

class WomenAPIView(APIView):
    def post(self, request):
        # print(request.data)
        
        post_new = Women.objects.create(
            title = request.data['title'],
            content = request.data['content'], 
            cat_id = request.data['cat_id']
        )
        return Response({'post':model_to_dict(post_new)})

