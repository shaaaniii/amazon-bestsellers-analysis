#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Class representing a fruit
class Fruit {
private:
    string name;
    int quantity;
    double ratePerFruit;

public:
    // Constructor to initialize fruit with name, quantity, and rate per fruit
    Fruit(string n, int q, double r) : name(n), quantity(q), ratePerFruit(r) {}

    // Function to display details of the fruit
    void displayFruitDetails() {
        cout << name << " -> Quantity: " << quantity
             << ", Rate per fruit: $" << ratePerFruit
             << ", Total cost: $" << getTotalCost() << endl;
    }

    // Function to get the total cost for the quantity of fruit
    double getTotalCost() {
        return quantity * ratePerFruit;
    }

    // Function to get the total quantity of the fruit
    int getQuantity() {
        return quantity;
    }
};

// Class representing the Fruit Basket
class FruitBasket {
private:
    vector<Fruit> fruits;

public:
    // Function to add a fruit to the basket
    void addFruit(Fruit fruit) {
        fruits.push_back(fruit);
    }

    // Function to display details of all fruits in the basket
    void displayBasket() {
        cout << "\nFruit Basket Contents:\n";
        for (Fruit& fruit : fruits) {
            fruit.displayFruitDetails();
        }
        cout << "Total number of fruits in the basket: " << getTotalNumberOfFruits() << endl;
    }

    // Function to calculate total number of fruits in the basket
    int getTotalNumberOfFruits() {
        int total = 0;
        for (Fruit& fruit : fruits) {
            total += fruit.getQuantity();
        }
        return total;
    }
};

int main() {
    // Creating a FruitBasket object
    FruitBasket basket;

    // Adding fruits to the basket
    basket.addFruit(Fruit("Apple", 5, 1.20));    // 5 apples, rate: $1.20 each
    basket.addFruit(Fruit("Mango", 3, 1.50));    // 3 mangoes, rate: $1.50 each
    basket.addFruit(Fruit("Banana", 6, 0.50));   // 6 bananas, rate: $0.50 each
    basket.addFruit(Fruit("Orange", 4, 0.80));   // 4 oranges, rate: $0.80 each

    // Displaying the details of the fruit basket
    basket.displayBasket();

    return 0;
}
