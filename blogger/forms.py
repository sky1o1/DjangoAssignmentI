from django.forms import ModelForm
from .models import Author, BlogTable


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', 'dob']


class BlogForm(ModelForm):
    class Meta:
        model = BlogTable
        fields = ['author', 'title', 'blog']