from django.shortcuts import render, get_object_or_404
from . models import Stock
from . serializers import StockSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def StockList(request):

	if request.method == 'GET':
		stock = Stock.objects.all()
		serializer  = StockSerializer(stock, many=True)
		return Response(serializer.data)

	if request.method =='POST':
		serializer = StockSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_created)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



