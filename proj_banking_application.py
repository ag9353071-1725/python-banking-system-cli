#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Banking Application
#Create Account
#view balance
#deposit money 
#withdraw money
#list account
#transfer funds 
#exit

#step1
#Generate account number - we have to create a function to get random account number 
import random
bank_account = {}


def generate_account_number():
    while True:
        account_number  = random.randint(100000,999999)
        if account_number not in bank_account:
            return account_number
#step 2
#create account number = writea function to create account number 

def create_account(name, initial_balance=0):
    account_number = generate_account_number()
    bank_account[account_number]={"name":name,"balance":initial_balance}
    print(f"Your Account created successfully,your account number is {account_number}")

#step 3
#view balance = we have to build a function to view balance then user can see the balance in her account number 

def view_balance(account_number):
    if account_number in bank_account:
        balance = bank_account[account_number]["balance"]
        print(f"your  balance is",{balance})
    else:
        print("Account does not exist")


#step 4 
#deposit money = we have a create a function , user can credit money in her account number

def deposit_money(account_number, amount):
    if account_number not in bank_account:
        print("Account doesnt exist")
        return
    if amount <=0:
        print("Deposit money must be positive")
        return

    bank_account[account_number]['balance']+=amount
    print("Your amount credited successfully")

#step 5 
#withdraw money = we have again create a  function , user can withdraw mpney from her bank account

def withdraw_money(account_number , amount):
    if account_number in bank_account:
        if bank_account[account_number]["balance"]>=amount:
            bank_account[account_number]['balance']-=amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficent funds")
    else:
        print("Account doesnt exist")

#step 6
#Transfer money = user can transer money from his account to her account 

def transfer_money(from_account, to_account, amount):
    if from_account not in bank_account or to_account not in bank_account:
        print("Account does not exist")
        return
    if bank_account[from_account]['balance']<amount:
        print(f"Insufficient funds, your current balance is {balance}")
        return
    bank_account[from_account]["balance"]-=amount
    bank_account[to_account]["balance"]+=amount
    balance = bank_account[from_account]["balance"]
    print(f"funds transfer successfully completed, your balance is {balance}")

#step 7 
#list account = check whether account number is in the bank account or not 

def list_account():
    if not  bank_account:
        print("account not created")
    else:
        for i in bank_account.items():
            print(i)
def main():
    while True:
        print("1.Create_account")
        print("2.View_Balance")
        print("3.Deposit_money")
        print("4.Withdraw_Money")
        print("5.Transfer_money")
        print("6.list_account")
        print("7.Exit")
        choice = int(input("Enter your choice,1-7"))
        if choice == 1:
            name=input("Enter your name:")
            initial_balance= input("Enter your initial_balance")

            if initial_balance.strip() == "":
                create_account(name) 
            else:
                initial_balance=int(initial_balance)
                create_account(name, initial_balance)

        elif choice == 2:
            account_number = int(input("Enter your account_number"))
            view_balance(account_number)
            account_number = int(input("Enter your account_number"))
            view_balance(account_number)

        elif choice == 3:
            account_number = int(input("Enter your account_number"))
            amount = int(input("Enter your amount"))
            deposit_money(account_number, amount)


        elif choice == 4:
            account_number = int(input("Enter your account_number"))
            amount = int(input("Enter your amount"))
            withdraw_money(account_number, amount)

        elif choice == 5:
            from_account = int(input("Enter your account number"))
            to_account = int(input("Enter her account_number"))
            amount = int(input("Enter amount"))
            transfer_money(from_account , to_account, amount)
            print("The amount has been transfer successfully")

        elif choice == 6:
            list_account()

        elif choice ==7:
            print("Thanks for using our browsebank")
        else:
            print("Invalid choice")

main()

















# In[ ]:




