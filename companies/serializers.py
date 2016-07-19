from . models import Stock,Issue 
from rest_framework import serializers

class StockSerializer(serializers.ModelSerializer):

	issued = serializers.StringRelatedField(many=True)

	class Meta:
		model = Stock
		fields = ('company_ticker','open_price', 'close_price', 'issued')

class IssueSerializer(serializers.ModelSerializer):

	class Meta:
		model = Issue
		fields = ('name', 'estimated_earning')

