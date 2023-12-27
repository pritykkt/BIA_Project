from django.db import models

class booklist(models.Model):
    book_name = models.CharField(max_length=200)
    book_price = models.FloatField()

    def __str__(self) -> str:
        return self.book_name
    