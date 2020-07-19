from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    dob = models.DateField()

    def __str__(self):
        return self.name


class BlogTable(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    blog = models.TextField(max_length=1000)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title