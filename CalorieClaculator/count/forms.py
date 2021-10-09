from . models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class FoodItemForm(ModelForm):
    class Meta:
        model = FoodItem
        fields = "__all__"

class AddUserFoodItem(ModelForm):
    class Meta:
        model = UserFoodItem
        fields = "__all__"

class CreateUserFoodItem(UserCreationForm):
    class Meta:
        model = UserFoodItem
        fields = ['name', 'email', 'password1', 'password2']