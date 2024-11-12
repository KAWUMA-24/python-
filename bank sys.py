import tkinter as tk
from tkinter import messagebox

class BankingAccount:
    def __init__(self, account_number, first_name, last_name, dob, email, phone, address):
        self.account_number = account_number
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.phone = phone
        self.address = address
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        messagebox.showinfo("Deposit Successful", f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            messagebox.showwarning("Insufficient Funds", "You do not have enough balance for this transaction.")
        else:
            self.balance -= amount
            messagebox.showinfo("Withdrawal Successful", f"Withdrew ${amount}. New balance: ${self.balance}")

    def get_details(self):
        return f"""
        Account Number: {self.account_number}
        First Name: {self.first_name}
        Last Name: {self.last_name}
        Date of Birth: {self.dob}
        Email: {self.email}
        Phone: {self.phone}
        Address: {self.address}
        Balance: ${self.balance}
        """

class BankingApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Banking Account System")
        self.geometry("400x500")
        self.accounts = {}

        self.create_widgets()

    def create_widgets(self):
        self.labels = [
            "Account Number:", "First Name:", "Last Name:", "Date of Birth:", "Email:",
            "Phone:", "Address:"
        ]
        self.entries = {}

        for i, label in enumerate(self.labels):
            tk.Label(self, text=label).grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
            entry = tk.Entry(self)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.entries[label] = entry

        # Separate entry for amount input
        tk.Label(self, text="Amount:").grid(row=len(self.labels), column=0, padx=10, pady=5, sticky=tk.W)
        self.amount_entry = tk.Entry(self)
        self.amount_entry.grid(row=len(self.labels), column=1, padx=10, pady=5)

        tk.Button(self, text="Create Account", command=self.create_account).grid(row=len(self.labels)+1, column=0, columnspan=2, pady=20)
        tk.Button(self, text="Deposit Money", command=self.deposit_money).grid(row=len(self.labels)+2, column=0, columnspan=2, pady=20)
        tk.Button(self, text="Withdraw Money", command=self.withdraw_money).grid(row=len(self.labels)+3, column=0, columnspan=2, pady=20)
        tk.Button(self, text="View Account Details", command=self.view_details).grid(row=len(self.labels)+4, column=0, columnspan=2, pady=20)

    def create_account(self):
        account_number = self.entries["Account Number:"].get()
        if account_number in self.accounts:
            messagebox.showwarning("Account Exists", "An account with this number already exists.")
        else:
            first_name = self.entries["First Name:"].get()
            last_name = self.entries["Last Name:"].get()
            dob = self.entries["Date of Birth:"].get()
            email = self.entries["Email:"].get()
            phone = self.entries["Phone:"].get()
            address = self.entries["Address:"].get()
            account = BankingAccount(account_number, first_name, last_name, dob, email, phone, address)
            self.accounts[account_number] = account
            messagebox.showinfo("Account Created", "Account successfully created!")

    def deposit_money(self):
        account_number = self.entries["Account Number:"].get()
        amount = float(self.amount_entry.get())
        if account_number in self.accounts:
            self.accounts[account_number].deposit(amount)
        else:
            messagebox.showwarning("Account Not Found", "No account found with this number.")

    def withdraw_money(self):
        account_number = self.entries["Account Number:"].get()
        amount = float(self.amount_entry.get())
        if account_number in self.accounts:
            self.accounts[account_number].withdraw(amount)
        else:
            messagebox.showwarning("Account Not Found", "No account found with this number.")

    def view_details(self):
        account_number = self.entries["Account Number:"].get()
        if account_number in self.accounts:
            details = self.accounts[account_number].get_details()
            messagebox.showinfo("Account Details", details)
        else:
            messagebox.showwarning("Account Not Found", "No account found with this number.")

if __name__ == "__main__":
    app = BankingApp()
    app.mainloop()
