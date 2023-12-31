from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    shelf = models.CharField(max_length=50)

    def __str__(self):
        return self.title
