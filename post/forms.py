from django import forms
from . import models
from post.models import Comment


class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'textarea', 'size': '40'}))
    slug = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))

    class Meta:
        model = models.Article   
        fields = ['title', 'text', 'slug', 'thumb']
    

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TextInput(attrs={
        'class':'textarea',
        'size':'40',
        'placeholder':'White your comment here...'
    }))

    class Meta:
        model = Comment
        fields = ['body',]