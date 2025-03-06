from django import forms
from delivery.models import Restaurant, Menu

class ResForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['res_name', 'Food_cat', 'rating', 'img', 'address']



class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ["res", "item_name", "description", "price", "is_available", "category"]

      