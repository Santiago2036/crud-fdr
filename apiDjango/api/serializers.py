from dataclasses import field, fields
from pyexpat import model
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import comentarios


class comentarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = comentarios
        fields = ('title', 'comentario', 'reaccion', 'fecha')
        ##read_only_fields = ('fecha', )

