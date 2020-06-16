from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
