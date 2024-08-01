from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["category","stock_name","quantity"]

    def clean(self):
        super(StockForm, self).clean()
        stock_name = self.cleaned_data.get('stock_name')
        if not stock_name:
            raise forms.ValidationError("Enter Stock Name")

        if len(stock_name) < 3:
            self.errors['stock_name'] = self.error_class([
               "Minimum of 3 characters required"
            ])

        for instance in Stock.objects.all():
            if instance.stock_name == stock_name:
                raise forms.ValidationError(stock_name + " Already Exist ")


class SearchForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["category","stock_name", "export_to_csv"]


class StockUpdate(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["category","stock_name", "quantity"]


class StockSell(forms.ModelForm):
    def clean_quantity_sold(self):
        quantity_sold = self.cleaned_data.get('quantity_sold')
        if quantity_sold < 1:
            raise forms.ValidationError("Quantity Sold must be at least 1 ")
        available_quantity = Stock.objects.get(pk=self.instance.pk).quantity
        if quantity_sold > available_quantity:
            raise forms.ValidationError("Not enough quantity available for sale")
        return quantity_sold

    class Meta:
        model = Stock
        fields = ["quantity_sold", "sold_by"]


class StockPurchase(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["quantity_purchased", "purchased_by"]


class ReorderLevel(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ["reorder_level"]


class StockDetailsDateFilter(forms.ModelForm):
    start_date = forms.DateTimeField(required=False)
    stop_date = forms.DateTimeField(required=False)

    class Meta:
        model = StockDetails
        fields = ["category", "stock_name", "start_date", "stop_date"]


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']
