from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Stock(models.Model):

	company_ticker = models.CharField(max_length=100)
	open_price = models.FloatField()
	close_price = models.FloatField()
	volume = models.IntegerField()

	def __str__(self):
		return self.company_ticker

class Issue(models.Model):

	# Many to One Relationship 
	name = models.ForeignKey(Stock, related_name='issued')
	date = models.DateTimeField(auto_now_add=True)
	estimated_earning = models.FloatField()

	def __unicode__(self):
		return '%s: %f' % (self.name, self.estimated_earning)

