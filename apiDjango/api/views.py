from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import comentarios
from .serializers import comentarioSerializer

# Create your views here.


class viewSetcomentario(viewsets.ModelViewSet):
        queryset = comentarios.objects.all()
        serializer_class = comentarioSerializer
