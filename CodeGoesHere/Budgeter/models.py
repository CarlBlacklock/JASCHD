from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Client(models.Model):
	#to be filled in
	def __str__(self):
		return self.user_id
	user_id = models.OneToOneField(User, on_delete=models.CASCADE, default = 1)
	user_bank_name = models.TextField()
	user_estimated_income = models.DecimalField(max_digits = 12, decimal_places = 2, default = 0.00)

class Transaction(models.Model):
	def __str__(self):
		return self.merchant_name
	TRANSACTION_TYPE_CHOICES = ()
	user_id = models.ForeignKey(Client, on_delete=models.CASCADE)
	transaction_date = models.DateField()
	merchant_name = models.TextField(default = 'Unknown')
	transaction_amount = models.DecimalField(max_digits = 12, decimal_places = 2, default = 0.00)


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
