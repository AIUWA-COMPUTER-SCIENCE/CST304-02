import math
import numpy as np
import matplotlib.pyplot as plt


# our changes
#  reject function
def rejectLoan(reason):
    print("Loan is rejected\n")
    print("reason:" + reason)
    exit()


NAME = input('What is your Name?:')
AGE = int(input('What is your Age?:'))

# cheking if the age is within parameters
if not (AGE >= 24 and AGE < 75):
    rejectLoan("Age Restriction")

SAL = int(input('What is your monthy Salary?'))
SAL = int(input('What is your monthy Salary?'))
RENT = int(input('What is your monthy RENT?:'))
SCH_FEES = int(input('What is your monthy Scool_Fees?:'))
FUEL = int(input('What is your monthy Fuel?:'))
FEEDING = int(input('What is your monthy Feeding?:'))
OTHER_INCOME = float(input('What is your OTHER INCOME?'))

TOTAL_EXPENSES = RENT+SCH_FEES+FUEL+FEEDING

# checking if the client is qualified for more cash.


LOAN_AMOUNT = int(input('What amount are you applying for?:'))
_35_OF_SALARY = 0.35 * SAL
_70_OF_SALARY = 0.70 * SAL
Fifty_percent_Sal = 0.5 * SAL

# if Temp_Expenses >
if TOTAL_EXPENSES <= (_35_OF_SALARY):

  if LOAN_AMOUNT <= (Fifty_percent_Sal):
    #if TOTAL_EXPENSES <= (0.35*SAL):
     print()
     print()
     print("LOAN Applican SUMARRY (RESULT)")
     print("==============================")
     print("Condition met")
     print("=============")
     print("1. Your Total Expenses is <= 35% of Salary")
     print("2. Your Loan Amount is <= 50% of Salary")
     print("------------------------------------------")
     print()
     print("Loan ACCEPTED")
     print("Amount approved is:",LOAN_AMOUNT)

  else:  # Loan application REJECTED
    print()
    print()
    print("LOAN Applican SUMARRY (RESULT)")
    print("==============================")

    print("Condition met")
    print("=============")
    print("1. Your Total Expenses is less than 35% of Salary")

    print("Reason for Rejection")
    print("====================")
    print("1. Your Loan Amount is greater than 50% of your Salary")

else:  # That is, IF the Loan Amount is > than 35% of Salary, then we must consider (check) whether
      # the applicant has substantial OTHER INCOME that exceeds 50% of the Salary (according to the existing rules)

    if OTHER_INCOME >= (0.5*SAL):  # That is, IF OTHER_INCOME of applicant exceeds 50% of Salary the two (2) lines of code below are executed
        print("LOAN Applican SUMARRY (RESULT)")
        print("==============================")
        print()
        print("Condition(s) met")
        print("=============")
        print("1. Your Other Income is > than 50% of Salary")
        print()
        print("Condition(s) NOT met")
        print("=============")
        print("1. Your Loan Amount is > 35% of Salary")
        print("--------------------------------------")
        print()
        print()
        print("CONGRATULATIONS......Loan ACCEPTED!!!!")
        print("Loan application Accepted_because your Other_Income is greater than 50% of your Salary")
        print()
        print("Reason for Acceptance")
        print("=====================")
        print("1. Your Other Income is greater than 50% of your Salary")

    else: #IF OTHER_INCOME of applicant DOES NOT exceeds 50% of Salary the two (2) lines of code below are executed
        print()
        print()
        print("Loan REJECTED")
        print("Rejected because of the following reasons:")
        print("1. The Amount you applied for is more than 35% of your Salary and")
        print("2. You do not have OTHER_INCOME that is greater than 50% of your Salary")


#TeLifTEMPORAL_AMOUNT =

#APPROVED_AMOUNT =










# See PyCharm help at https://www.jetbrains.com/help/pycharm/

