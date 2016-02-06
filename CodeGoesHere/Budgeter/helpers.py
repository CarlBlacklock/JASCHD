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
		newTransaction = model.Transaction(transaction_date = row['DATE'], merchant_name = row['TRASACTION DETAILS'], transaction_amount = row['DEBIT'])
		newTransaction.save(force_insert = True)

