from django.db.models import fields
from rest_framework import serializers
from .models import booklist
 
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = booklist
        fields = ('book_name', 'book_price')