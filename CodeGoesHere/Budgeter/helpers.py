import Budgeter.models as model
from django.db import models
import csv
from decimal import *

#helper functions to handle various data processing functions

def getTransactionsFromFile(path_to_file):
	transactionDict = csv.DictReader(open(path_to_file), delimiter = '\t')
	rawTransactions = []
	for row in transactionDict:
		rawTransactions.append(row)
	return rawTransactions

def transactionFormatAndSave(rawTransactions, user_id):
	for row in rawTransactions:
		dateString = row['DATE']
		tokenizedString = dateString.split('/')
		if len(tokenizedString[1]) == 1:
			formatedDay = '0'+tokenizedString[1]
		else:
			formatedDay = tokenizedString[1]

		if len(tokenizedString[0]) == 1:
			formatedMonth = '0'+tokenizedString[0]
		else:
			formatedMonth = tokenizedString[0]
		formatedDate = tokenizedString[2]+'-'+formatedMonth+'-'+formatedDay
		if row['DEBIT'] != '':
			newTransaction = model.Transaction(transaction_date = formatedDate, merchant_name = row['TRANSACTION DETAILS'], transaction_amount = Decimal(row['DEBIT']), user_id = user_id)
			newTransaction.save(force_insert = True)

def transactionCatagorization(user_id, monthToCatagorize):
	all_catagories = model.TransactionCatagories.objects.all()
	catagorized_spending = {}
	for entry in all_catagories:
		catagorized_spending[entry] = Decimal(0.00)

	user_transactions = model.Transaction.objects.filter(user_id)

	for entry in user_transactions:
		catagory = model.TransactionCatagories.objects.filter(entry[merchant_name])
		catagorized_spending[merchant_name] = Decimal(catagorized_spending[merchant_name]) + Decimal(user_transactions[transaction_amount])

	return catagorized_spending