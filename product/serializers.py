
from dataclasses import fields
from django.core import serializers
from rest_framework import routers, serializers, viewsets

from product.models import product_mod



class productserializer(serializers.ModelSerializer):
    class Meta:
        model=product_mod
        fields='__all__'