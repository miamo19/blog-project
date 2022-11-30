from django import forms
from django.forms import TextInput, Textarea

from .models import Comment



class CommentForm(forms.ModelForm):
    username = forms.CharField(max_length=40, widget=TextInput(attrs={"class":"form-control"}))
    email    = forms.EmailField(widget=TextInput(attrs={"class": "form-control" }))
    body     = forms.CharField(max_length=70, widget=Textarea(attrs={"class": "form-control",
                                                      'rows':3,
                                                      "placeholder":"Join the discussion and leave a comment!"
                                                      }))
    class Meta:
        model  = Comment
        fields = ['username', 'email', 'body']
