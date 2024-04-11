from rest_framework import generics
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Women
from .serializers import WomenSerializer


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# simple realization of API request without serializer
class WomenAPIView(APIView):
    def get(self, request):
        lst = Women.objects.all().values()
        return Response({"posts": list(lst)})

    def post(self, request, *args, **kwargs):
        return Response({"title": "Jehnifer"})
