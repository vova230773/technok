from itertools import product
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import routers, serializers, viewsets
from core.views import CustomHtmxMixin
from product.models import product_mod
from product.serializers import productserializer

class CreateProduct(CustomHtmxMixin, TemplateView):
    template_name = "product_list.html"

    def get_context_data(self, **kwargs):
        kwargs["title"] = "Список товарів"
        return super().get_context_data(**kwargs)

class productApiView(viewsets.ModelViewSet):
    queryset=product_mod.objects.all()
    serializer_class=productserializer
    http_method_names=['get']



