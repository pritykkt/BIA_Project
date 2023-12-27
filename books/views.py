from .models import booklist
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import booklist
from .serlializers import BookSerializer
from django.shortcuts import  get_object_or_404
from rest_framework import serializers
from rest_framework import status
 


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Add': '/create',
        'Delete': '/item/pk/delete'
    }
 
    return Response(api_urls)

@api_view(['POST'])
def add_items(request):
    item = BookSerializer(data=request.data)
 
    # validating for already existing data
    if booklist.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
 
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def view_items(request):
     
    if request.query_params:
        items = booklist.objects.filter(**request.query_params.dict())
    else:
        items = booklist.objects.all()
 
    if items:
        serializer = BookSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request, pk):
    item = get_object_or_404(booklist, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
