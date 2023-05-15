

#  //////////////////////////////
#  python manage.py shell  
#  >>> from myapp.serrializers import encode, decode 
#  >>> encode()
#  >>> decode()

# from rest_framework import serializers
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# import io


# class WomenModel:
#     def __init__(self, title, content):
#         self.title=title
#         self.content=content

# class WomenSerializer(serializers.Serializer):
#     title=serializers.CharField(max_length=255)
#     content=serializers.CharField()


# def encode():
#     model=WomenModel('isim','Ilhom')
#     model_sr=WomenSerializer(model) 
#     print(model_sr.data,type(model_sr.data),sep='\n')
#     json=JSONRenderer().render(model_sr.data)
#     print(json)
    
    
# def decode():
#     stream=io.BytesIO(b'{"title":"isim","content":"Ilhom"}')
#     data=JSONParser().parse(stream)
#     serializer=WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)



# 1)  //////////////////////////////////////      
# from rest_framework import serializers

# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()


#  2)  //////////////////////////////////////

# from rest_framework import serializers
# from .models import Women

# class WomenSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()


#     def create(self,validated_data):
#         return Women.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.time_update = validated_data.get('time_update', instance.time_update)
#         instance.is_published = validated_data.get('is_published', instance.is_published)
#         instance.cat_id = validated_data.get('cat_id', instance.cat_id)
#         instance.save()
#         return instance 


# /////////////////  3), 4), 5), 6), 7), 8), 9), 10) / ////////////////
from rest_framework import serializers
from .models import Women


class WomenModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Women
        fields=('pk','title','content','cat')
        
    
