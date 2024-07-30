from django.shortcuts import render
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .serializer import FilterCategoriesSerializer, FiltersSerializer, PeriodFilterSerializer
from .models import FilterCategories, Filters, PeriodFilter


class FilterCategoryAPIView(generics.ListAPIView):
    queryset = FilterCategories.objects.all()
    serializer_class = FilterCategoriesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category"]


class FiltersAPIView(generics.ListAPIView):
    queryset = Filters.objects.all()
    serializer_class = FiltersSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["filter_category"]


class PeriodFilterAPIView(generics.ListAPIView):
    queryset = PeriodFilter.objects.all()
    serializer_class = PeriodFilterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category"]
