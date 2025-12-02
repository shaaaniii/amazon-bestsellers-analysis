#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <limits>

using namespace std;

// Color codes for terminal output
#define RESET   "\033[0m"
#define RED     "\033[31m"
#define GREEN   "\033[32m"
#define YELLOW  "\033[33m"
#define BLUE    "\033[34m"
#define WHITE   "\033[37m"
#define BG_BLUE "\033[44m"

// Account class to store account details
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
        cout << GREEN << "Deposited: " << amount << RESET << endl;
    }

    bool withdraw(double amount) {
        if (amount > balance) {
            cout << RED << "Insufficient balance!" << RESET << endl;
            return false;
        }
        balance -= amount;
        cout << GREEN << "Withdrawn: " << amount << RESET << endl;
        return true;
    }

    void changePin(string newPin) {
        pin = newPin;
        cout << GREEN << "PIN changed successfully!" << RESET << endl;
    }

    bool validatePin(string inputPin) {
        return pin == inputPin;
    }

    void displayAccountDetails() {
        cout << BG_BLUE << WHITE << "Account Number: " << accountNumber << RESET << endl;
        cout << BG_BLUE << WHITE << "Account Holder Name: " << accountHolderName << RESET << endl;
        cout << BG_BLUE << WHITE << "Current Balance: " << balance << RESET << endl;
    }
};

// Transaction class to log transactions
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
            cout << RED << "Unable to open file!" << RESET << endl;
        }
    }
};

// ATM class to manage the bank accounts
class ATM {
private:
    vector<Account> accounts;

public:
    void createAccount(string accNum, string accHolder, double initialBalance, string accountPin) {
        if (accNum.length() != 10 || accountPin.length() != 4) {
            cout << RED << "Account number must be 10 digits and PIN must be 4 digits." << RESET << endl;
            return;
        }

        Account newAccount(accNum, accHolder, initialBalance, accountPin);
        accounts.push_back(newAccount);
        cout << GREEN << "Account created successfully!" << RESET << endl;
    }

    Account* findAccount(string accNum) {
        for (auto& account : accounts) {
            if (account.getAccountNumber() == accNum) {
                return &account;
            }
        }
        return nullptr;
    }

    void deposit(string accNum, double amount) {
        Account* account = findAccount(accNum);
        if (account) {
            account->deposit(amount);
            Transaction transaction(accNum, "Deposit", amount);
            transaction.logTransaction();
        } else {
            cout << RED << "Account not found!" << RESET << endl;
        }
    }

    void withdraw(string accNum, double amount) {
        Account* account = findAccount(accNum);
        if (account) {
            if (account->withdraw(amount)) {
                Transaction transaction(accNum, "Withdraw", amount);
                transaction.logTransaction();
            }
        } else {
            cout << RED << "Account not found!" << RESET << endl;
        }
    }

    void checkBalance(string accNum) {
        Account* account = findAccount(accNum);
        if (account) {
            cout << "Current Balance: " << account->getBalance() << endl;
        } else {
            cout << RED << "Account not found!" << RESET << endl;
        }
    }

    void viewTransactionHistory() {
        ifstream inFile("transactions.txt");
        string line;
        if (inFile.is_open()) {
            while (getline(inFile, line)) {
                cout << line << endl;
            }
            inFile.close();
        } else {
            cout << RED << "Unable to open file!" << RESET << endl;
        }
    }

    void transferFunds(string fromAccNum, string toAccNum, double amount) {
        Account* fromAccount = findAccount(fromAccNum);
        Account* toAccount = findAccount(toAccNum);
        if (fromAccount && toAccount) {
            if (fromAccount->withdraw(amount)) {
                toAccount->deposit(amount);
                Transaction transaction(fromAccNum, "Transfer to " + toAccNum, amount);
                transaction.logTransaction();
                cout << GREEN << "Transfer successful!" << RESET << endl;
            }
        } else {
            cout << RED << "One or both accounts not found!" << RESET << endl;
        }
    }

    void deleteAccount(string accNum) {
        for (auto it = accounts.begin(); it != accounts.end(); ++it) {
            if (it->getAccountNumber() == accNum) {
                accounts.erase(it);
                cout << GREEN << "Account deleted successfully!" << RESET << endl;
                return;
            }
        }
        cout << RED << "Account not found!" << RESET << endl;
    }
};

// Main function to drive the ATM system
int main() {
    ATM atm;
    int choice;
    string accNum, accHolder, accountPin, toAccNum;
    double amount;

    while (true) {
        cout << BG_BLUE << WHITE << "ATM Management System" << RESET << endl;
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

        if (!(cin >> choice)) {
            cout << RED << "Invalid input! Please enter a valid choice." << RESET << endl;
            cin.clear();  // Clear the error flag
            cin.ignore(numeric_limits<streamsize>::max(), '\n');  // Discard invalid input
            continue;  // Prompt again
        }

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
                    cout << RED << "Account not found!" << RESET << endl;
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
                    cout << RED << "Account not found!" << RESET << endl;
                }
                break;
            }

            case 10: {
                cout << "Exiting..." << endl;
                return 0;  // Exit the program
            }

            default: {
                cout << RED << "Invalid choice! Please try again." << RESET << endl;
                break;
            }
        }
    }
}


