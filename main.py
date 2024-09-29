employeeName = input("Employee's Name: ")
numShifts = int(input("Number of Shifts: "))
numTransactions = int(input("Number of Transactions: "))
transactionDollarValue = float(input("Transaction Dollar Value: "))

productivityScore = (float(transactionDollarValue)/int(numTransactions)/int(numShifts))

if productivityScore <= 30:
  bonus = 50.00
elif 31 <= productivityScore <= 69:
  bonus = 75.00
elif 70 <= productivityScore <= 199:
  bonus = 100.00
else:
  bonus = 200.00

print("Employee Name: " + str(employeeName))
print("Employee Bonus: $" + str(bonus))