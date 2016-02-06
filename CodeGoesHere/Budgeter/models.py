from django.db import models

# Create your models here.

class User(models.Model):
	#to be filled in
	user_id = models.EmailField(max_length = 254, primary_key = True)
	user_name = models.TextField()
	user_bank_name = models.TextField()

class Transaction(models.Model):
	TRANSACTION_TYPE_CHOICES = ()
	transaction_date = models.DateField()
	transaction_type = models.


class TransactionCatagories(models.Model):
	TRANSACTION_CATAGORY_CHOICES = (
		('STAPLEFOOD', 'Staple Food'),
		('ENTERTAINMENT', 'Entertainment'),
		('ELECTRONICS', 'Electronics'),
		('OTHERFOOD', 'Other Food'),
		('CLOTHING', 'Clothing'),
		('TRANSPORTATION', 'Transportation')
		)
	merchant_name = models.TextField()
	merchant_catagory = models.TextField(choices = TRANSACTION_CATAGORY_CHOICES)
