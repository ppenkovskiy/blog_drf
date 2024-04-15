from django.forms import model_to_dict
from rest_framework import generics
from rest_framework import serializers
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Women
from .serializers import WomenSerializer


# Simple realization of API request without serializer
class WomenAPIView(APIView):
    def get(self, request):
        w = Women.objects.all()
        return Response({"posts": WomenSerializer(w, many=True).data})

    def post(self, request, *args, **kwargs):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id'],
        )

        return Response({"post": WomenSerializer(post_new).data})
