from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

class User(models.Model):
	#to be filled in
	def __str__(self):
		return self.user_name
	user_id = models.EmailField(max_length = 254, primary_key = True)
	user_name = models.TextField()
	user_bank_name = models.TextField()

class Transaction(models.Model):
	def __str__(self):
		return self.merchant_name
	TRANSACTION_TYPE_CHOICES = ()
	transaction_date = models.DateField()
	transaction_type = models.TextField()
	merchant_name = models.TextField()
	transaction_amount = models.DecimalField(max_digits = 12, decimal_places = 2)


class TransactionCatagories(models.Model):
	TRANSACTION_CATAGORY_CHOICES = (
		('STAPLEFOOD', 'Staple Food'),
		('ENTERTAINMENT', 'Entertainment'),
		('ELECTRONICS', 'Electronics'),
		('OTHERFOOD', 'Other Food'),
		('CLOTHING', 'Clothing'),
		('TRANSPORTATION', 'Transportation')
		)
	def __str__(self):
		return self.merchant_catagory
	merchant_name = models.TextField()
	merchant_catagory = models.TextField(choices = TRANSACTION_CATAGORY_CHOICES)
