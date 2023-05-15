

# """  

# """

# from rest_framework import serializers

# class CommentSerializer(serializers.Serializer):
#     email=serializers.EmailField()
#     content=serializers.CharField()

#     def validate_content(self,value):
#         #If content is 'baz' returns 'foo'
#         if value and value == "baz":
#             return "foo"
#         return value

# """       
# Let's try with wrong values (for email):

# >>> serializer = CommentSerializer(data={'email': 'foobar', 'content': 'baz'})

# >>> serializer.initial_data
# {'content': 'baz', 'email': 'foobar'}

# >>> serializer.is_valid()
# False

# >>> serializer.validated_data
# {}

# >>> serializer.errors
# {'email': [u'Enter a valid email address.']}


# Now Let's try with correct values

# >>> serializer2 = CommentSerializer(data={'email': 'foobar@email.it', 
# 'content': 'baz'})  
# >>> serializer2.is_valid()
# True

# >>> serializer2.initial_data
# {'content': 'baz', 'email': 'foobar@email.it'}
# >>> serializer2.errors
# {}

# >>> serializer2.data
# {'content': u'foo', 'email': u'foobar@email.it'}

# >>> serializer2.validated_data
# OrderedDict([(u'email', u'foobar@email.it'), (u'content', u'foo')])

# So:

# data : is a dict and you can see it only after is_valid() (you can see only not validated values)
# validated_data is an OrderedDict and you can see it only after is_valid() and is_valid() == True


# """

