# coding=utf-8
from django import forms
from models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'msg', 'publishTime', 'coverImg', 'contentImg']

    coverImg = forms.FileField(
        label='Select a cover image:',
        help_text=''
    )

    contentImg = forms.FileField(
        label='Select a content image:',
        help_text=''
    )
