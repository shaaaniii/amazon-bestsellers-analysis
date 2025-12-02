#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

int main() {
    int n;

    // Accept the size of the array
    cout << "Enter the size of the array: ";
    cin >> n;

    vector<int> arr(n);
    unordered_set<int> uniqueValues;
    unordered_set<int> duplicates;
    
    // Accept values into the array
    cout << "Enter " << n << " values:\n";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // Display values with their positions
    cout << "\nValues and their positions:\n";
    for (int i = 0; i < n; i++) {
        cout << "Position " << i + 1 << ": " << arr[i] << endl;
    }

    // Find duplicate values
    for (int i = 0; i < n; i++) {
        if (uniqueValues.find(arr[i]) != uniqueValues.end()) {
            duplicates.insert(arr[i]);
        } else {
            uniqueValues.insert(arr[i]);
        }
    }

    // Display the number of duplicate values
    cout << "\nNumber of duplicate values: " << duplicates.size() << endl;

    // Remove duplicate values and display the array
    cout << "\nArray after removing duplicates:\n";
    uniqueValues.clear();
    for (int i = 0; i < n; i++) {
        if (uniqueValues.find(arr[i]) == uniqueValues.end()) {
            cout << arr[i] << " ";
            uniqueValues.insert(arr[i]);
        }
    }
    cout << endl;

    return 0;
}

	
	
	

