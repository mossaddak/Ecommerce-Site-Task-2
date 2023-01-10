from django import forms
from .models import (
    Products,
    ProductFeedback
)
from django.forms import ModelForm


#Add Product =====================================================
class AddProduct(forms.ModelForm):
    #product_desc = RichTextField()

    class Meta:
        model = Products
        fields = ('title','description','price','image')
        
        labels = {
            'title':'Product Title',
            'description':'Description',
            'price':'Price',
            'image':'Product Image',
        }

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'style':'font-size:13px;', 'required': True}),
            'description':forms.Textarea(attrs={'class':'form-control', 'style':'font-size:13px;','cols':'3'}),
            'price':forms.NumberInput(attrs={'class':'form-control', 'style':'font-size:13px;', 'min':'1', 'required': True}),
            'image':forms.FileInput(attrs={'class':'form-control', 'style':'font-size:13px;', 'required': True})
        }


#Add Product =====================================================
class UpdateProductForm(forms.ModelForm):

    class Meta:
        model = Products
        fields = ('title','description','price','image')        

        labels = {
            'title':'Product Title',
            'description':'Description',
            'price':'Price',
            'image':'Product Image',
        }

         

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'style':'font-size:13px;', 'required': True}),
            'description':forms.Textarea(attrs={'class':'form-control', 'style':'font-size:13px;','cols':'3'}),
            'price':forms.NumberInput(attrs={'class':'form-control', 'style':'font-size:13px;', 'min':'1', 'required': True}),
            'image':forms.FileInput(attrs={'class':'form-control', 'style':'font-size:13px;', 'required': True})
        }

    
    #update feedback form____________________________
class UpdateFeedbackForm(forms.ModelForm):

    class Meta:
        model = ProductFeedback
        fields = ('rating','feedBACK')