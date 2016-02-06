import Budgeter.models as model
from django.db import models
import csv

#helper functions to handle various data processing functions

def getTransactionsFromFile(path_to_file):
	transactionDict = csv.DictReader(open(path_to_file), delimiter = '\t')
	rawTransactions = []
	for row in transactionDict:
		rawTransactions.append(row)
	return rawTransactions

def transactionFormatAndSave(rawTransactions):
	for row in rawTransactions:
		dateString = row['DATE']
		tokenizedString = dateString.split('/')
		if len(tokenizedString[0]) == 1:
			formatedDay = '0'+tokenizedString[0]
		else:
			formatedDay = tokenizedString[0]

		if len(tokenizedString[1]) == 1:
			formatedMonth = '0'+tokenizedString[1]
		else:
			formatedMonth = tokenizedString[1]
		formatedDate = tokenizedString[2]+'-'+formatedMonth+'-'+formatedDay
		newTransaction = model.Transaction(transaction_date = formatedDate, merchant_name = row['TRANSACTION DETAILS'], transaction_amount = row['DEBIT'])
		newTransaction.save(force_insert = True)

