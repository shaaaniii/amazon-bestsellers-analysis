
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

class Account {
private:
    string accountNumber;
    string accountHolderName;
    double balance;
    string pin;

public:
    Account(string accNum, string accHolder, double initialBalance, string accountPin) {
        accountNumber = accNum;
        accountHolderName = accHolder;
        balance = initialBalance;
        pin = accountPin;
    }

    string getAccountNumber() {
        return accountNumber;
    }

    string getAccountHolderName() {
        return accountHolderName;
    }

    double getBalance() {
        return balance;
    }

    void deposit(double amount) {
        balance += amount;
        cout << "Deposited: " << amount << endl;
    }

    bool withdraw(double amount) {
        if (amount > balance) {
            cout << "Insufficient balance!" << endl;
            return false;
        }
        balance -= amount;
        cout << "Withdrawn: " << amount << endl;
        return true;
    }

    void changePin(string newPin) {
        pin = newPin;
        cout << "PIN changed successfully!" << endl;
    }

    bool validatePin(string inputPin) {
        return pin == inputPin;
    }

    void displayAccountDetails() {
        cout << "Account Number: " << accountNumber << endl;
        cout << "Account Holder Name: " << accountHolderName << endl;
        cout << "Current Balance: " << balance << endl;
    }
};

class Transaction {
private:
    string accountNumber;
    string transactionType;
    double amount;

public:
    Transaction(string accNum, string type, double amt) {
        accountNumber = accNum;
        transactionType = type;
        amount = amt;
    }

    void logTransaction() {
        ofstream outFile("transactions.txt", ios::app);
        if (outFile.is_open()) {
            outFile << "Account Number: " << accountNumber << ", "
                    << "Transaction Type: " << transactionType << ", "
                    << "Amount: " << amount << endl;
            outFile.close();
        } else {
            cout << "Unable to open file!" << endl;
        }
    }
};

class ATM {
private:
    vector<Account> accounts;
    bool isAccountCreated = false;  // Flag to check if an account is created

public:
    void createAccount(string accNum, string accHolder, double initialBalance, string accountPin) {
        Account newAccount(accNum, accHolder, initialBalance, accountPin);
        accounts.push_back(newAccount);
        isAccountCreated = true; // Set flag to true once account is created
        cout << "Account created successfully!" << endl;
    }

    Account* findAccount(string accNum) {
        for (auto& account : accounts) {
            if (account.getAccountNumber() == accNum) {
                return &account;
            }
        }
        return nullptr;
    }

    // Function to check if an account is created before any action
    bool checkAccountCreated() {
        return isAccountCreated;
    }

    void deposit(string accNum, double amount) {
        if (!checkAccountCreated()) {
            cout << "Please create an account first!" << endl;
            return;
        }
        Account* account = findAccount(accNum);
        if (account) {
            account->deposit(amount);
            Transaction transaction(accNum, "Deposit", amount);
            transaction.logTransaction();
        } else {
            cout << "Account not found!" << endl;
        }
    }

    void withdraw(string accNum, double amount) {
        if (!checkAccountCreated()) {
            cout << "Please create an account first!" << endl;
            return;
        }
        Account* account = findAccount(accNum);
        if (account) {
            if (account->withdraw(amount)) {
                Transaction transaction(accNum, "Withdraw", amount);
                transaction.logTransaction();
            }
        } else {
            cout << "Account not found!" << endl;
        }
    }

    void checkBalance(string accNum) {
        if (!checkAccountCreated()) {
            cout << "Please create an account first!" << endl;
            return;
        }
        Account* account = findAccount(accNum);
        if (account) {
            cout << "Current Balance: " << account->getBalance() << endl;
        } else {
            cout << "Account not found!" << endl;
        }
    }

    void viewTransactionHistory() {
        if (!checkAccountCreated()) {
            cout << "Please create an account first!" << endl;
            return;
        }
        ifstream inFile("transactions.txt");
        string line;
        if (inFile.is_open()) {
            while (getline(inFile, line)) {
                cout << line << endl;
            }
            inFile.close();
        } else {
            cout << "Unable to open file!" << endl;
        }
    }

    void transferFunds(string fromAccNum, string toAccNum, double amount) {
        if (!checkAccountCreated()) {
            cout << "Please create an account first!" << endl;
            return;
        }
        Account* fromAccount = findAccount(fromAccNum);
        Account* toAccount = findAccount(toAccNum);
        if (fromAccount && toAccount) {
            if (fromAccount->withdraw(amount)) {
                toAccount->deposit(amount);
                Transaction transaction(fromAccNum, "Transfer to " + toAccNum, amount);
                transaction.logTransaction();
                cout << "Transfer successful!" << endl;
            }
        } else {
            cout << "One or both accounts not found!" << endl;
        }
    }

    void deleteAccount(string accNum) {
        if (!checkAccountCreated()) {
            cout << "Please create an account first!" << endl;
            return;
        }
        for (auto it = accounts.begin(); it != accounts.end(); ++it) {
            if (it->getAccountNumber() == accNum) {
                accounts.erase(it);
                cout << "Account deleted successfully!" << endl;
                return;
            }
        }
        cout << "Account not found!" << endl;
    }
};

int main() {
    ATM atm;
    int choice;
    string accNum, accHolder, accountPin, toAccNum;
    double amount;

    while (true) {
        cout << "ATM Management System" << endl;
        cout << "1. Create Account" << endl;
        cout << "2. Deposit" << endl;
        cout << "3. Withdraw" << endl;
        cout << "4. Check Balance" << endl;
        cout << "5. View Transaction History" << endl;
        cout << "6. Transfer Funds" << endl;
        cout << "7. Change PIN" << endl;
        cout << "8. Delete Account" << endl;
        cout << "9. View Account Details" << endl;
        cout << "10. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1: {
                cout << "Enter Account Number (10 digits): ";
                cin >> accNum;
                cout << "Enter Account Holder Name: ";
                cin >> accHolder;
                cout << "Enter Initial Balance: ";
                cin >> amount;
                cout << "Enter Account PIN (4 digits): ";
                cin >> accountPin;
                atm.createAccount(accNum, accHolder, amount, accountPin);
                break;
            }

            case 2: {
                cout << "Enter Account Number: ";
                cin >> accNum;
                cout << "Enter Amount to Deposit: ";
                cin >> amount;
                atm.deposit(accNum, amount);
                break;
            }

            case 3: {
                cout << "Enter Account Number: ";
                cin >> accNum;
                cout << "Enter Amount to Withdraw: ";
                cin >> amount;
                atm.withdraw(accNum, amount);
                break;
            }

            case 4: {
                cout << "Enter Account Number: ";
                cin >> accNum;
                atm.checkBalance(accNum);
                break;
            }

            case 5: {
                atm.viewTransactionHistory();
                break;
            }

            case 6: {
                cout << "Enter Your Account Number: ";
                cin >> accNum;
                cout << "Enter Recipient Account Number: ";
                cin >> toAccNum;
                cout << "Enter Amount to Transfer: ";
                cin >> amount;
                atm.transferFunds(accNum, toAccNum, amount);
                break;
            }

            case 7: {
                cout << "Enter Account Number: ";
                cin >> accNum;
                cout << "Enter New PIN: ";
                cin >> accountPin;
                Account* account = atm.findAccount(accNum);
                if (account) {
                    account->changePin(accountPin);
                } else {
                    cout << "Account not found!" << endl;
                }
                break;
            }

            case 8: {
                cout << "Enter Account Number: ";
                cin >> accNum;
                atm.deleteAccount(accNum);
                break;
            }

            case 9: {
                cout << "Enter Account Number: ";
                cin >> accNum;
                Account* account = atm.findAccount(accNum);
                if (account) {
                    account->displayAccountDetails();
                } else {
                    cout << "Account not found!" << endl;
                }
                break;
            }

            case 10: {
                cout << "Exiting..." << endl;
                return 0;
            }

            default: {
                cout << "Invalid choice! Please try again." << endl;
                break;
            }
        }
    }
}

