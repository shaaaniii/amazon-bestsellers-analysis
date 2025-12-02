"""Design a Python class named `BankAccount` to represent bank accounts. 
Theory: A bank account typically includes attributes such as account number, balance, and account holder name. 
The class should handle operations such as deposit, withdrawal, and transfer of funds between accounts. 
Operations: 1. Deposit: Add funds to the account 
2. Withdrawal: Subtract funds from the account 
3. Transfer: Transfer funds from one account to another 
Test Cases: Test Case 1: acc1 = BankAccount("John Doe", 1000) acc2 = BankAccount("Jane Smith", 2000) 
assert acc1.balance == 1000 assert acc2.balance == 2000 
acc1.deposit(500) acc2.withdraw(100) acc1.transfer(acc2, 200) 
assert acc1.balance == 1300 assert acc2.balance == 2300 
Test Case 2: acc3 = BankAccount("Alice Johnson", 500) 
acc4 = BankAccount("Bob Brown", 1500) assert acc3.balance == 500 
assert acc4.balance == 1500 acc3.deposit(100) acc4.withdraw(200) 
acc3.transfer(acc4, 300) assert acc3.balance == 400 assert acc4.balance == 1800 """
class BankAccount:
    def __init__(self,accnumber,holdername,sender , reciever,balance = 0):
        self.accnumber = accnumber
        self.balance = balance
        self.holdername = holdername
        self.sender = sender
        self.reciever = reciever

    def deposit_amount(self,amount):
         self.balance+=amount
         print(f"{amount}is deposited .new balance is {self.balance}")

    def withdrawal(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
            print(f"{amount} is withdrawn. new balance is {self.balance}")
    
    def transfer_amount(self,sender, receiver, amount):
    if sender not in accounts or receiver not in accounts:
        return "Error: One or both accounts do not exist."
    if accounts[sender] < amount:
        return "Error: Insufficient balance in sender's account."
    
    # Perform the transfer
    accounts[sender] -= amount
    accounts[receiver] += amount
    return f"Transfer successful! New balances:\n{sender}: {accounts[sender]}\n{receiver}: {accounts[receiver]}"

 

