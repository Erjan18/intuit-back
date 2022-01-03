from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.viewsets import ModelViewSet



class HeadView(APIView):
    def get(self,*args,**kwargs):
        name = Header.objects.all()
        serializer = HeaderSerializers(name,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class HeadisView(viewsets.ModelViewSet):
    queryset = Headerdis.objects.all()
    serializer_class = HeaderdisSerialzers