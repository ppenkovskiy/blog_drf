import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Women


# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField()
    time_update = serializers.DateTimeField()
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()


# def encode():
#     model = WomenModel('Women_1', 'Content_1')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Women_1","content":"Content_1"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data) # dict