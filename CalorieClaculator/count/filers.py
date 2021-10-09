import django_filters
from . models import *

class FoodItemFilter(django_filters.FilterSet):
    class Meta:
        model = Fooditem
        fields = ['name']