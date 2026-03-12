#/ ATM withdrawal system
#real life analogy:ATM check if balance is enough before giving cash.
#problem:
#take account balance and withdrawal amount as input 
#condition : if withdrawal amount is less than or equal to balance then print "withdrawal successful" and update balance

balance = float(input("Enter account balance: "))
withdrawal_amount = float(input("Enter withdrawal amount: "))   
if withdrawal_amount <= balance:
    balance -= withdrawal_amount
    print("Withdrawal successful. Updated balance:", balance)
else:
    print("Insufficient balance. Withdrawal failed.")

        