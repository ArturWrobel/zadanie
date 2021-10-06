from django.db import models

class Article (models.Model):
    title = models.TextField(max_length=100)
    content = models.TextField(max_length=300)