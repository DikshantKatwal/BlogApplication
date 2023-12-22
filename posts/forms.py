from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'desc']
        widgets = {
            'desc': forms.Textarea(attrs={'cols': 80, 'rows': 10, 'required': True}),
        }
