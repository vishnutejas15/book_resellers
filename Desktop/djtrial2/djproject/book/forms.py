from django import forms
from django.contrib.auth.models import User
from book import models

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=('username','first_name','last_name','email','password')
        widgets={
                  'username':forms.TextInput(attrs={'class':'form-control','autofocus':'True'}),
                  'first_name':forms.TextInput(attrs={'class':'form-control'}),
                  'last_name':forms.TextInput(attrs={'class':'form-control'}),
                  'Email':forms.EmailInput(attrs={'class':'form-control'}),
        }


class adminform(forms.Form):
    un=forms.CharField(label='username',widget=forms.TextInput(attrs={'class':'form-control','maxlength':'20','placeholder':'username'}))
    pw=forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class':'form-control','maxlength':'20','placeholder':'password'}))


class sellbookform(forms.ModelForm):
    class Meta:
        model=models.owner
        fields=('book_name','original_price','selling_price','address','ph_num','bookpassword','ownername')
        widgets={
            'ownername':forms.TextInput(attrs={'class':'form-control','autofocus':'True'}),
            'book_name':forms.TextInput(attrs={'class':'form-control',}),
            'original_price':forms.TextInput(attrs={'class':'form-control','pattern':'[0-9]+'}),
            'selling_price':forms.TextInput(attrs={'class':'form-control','pattern':'[0-9]+'}),
            'address':forms.TextInput(attrs={'class':'form-control','maxlength':'100'}),
            'ph_num':forms.TextInput(attrs={'class':'form-control','maxlength':'100','pattern':'[6-9]{1}[0-9]{9}'}),
            'bookpassword':forms.TextInput(attrs={'class':'form-control','maxlength':'100'}),
        }

class booksearchForm(forms.Form):
    q=forms.CharField(label='',
    widget=forms.TextInput(attrs={'class':'form-control','maxlength':'30','placeholder':'search'}),
    )
