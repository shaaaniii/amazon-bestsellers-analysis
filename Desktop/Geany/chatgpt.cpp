#include<iostream>
using namespace std;

// Forward declaration of the class Sphere to use it inside Cuboid class
class Sphere;

// Outer class Sphere
class Sphere {
private:
    int radius;
    double volume, surface_area;

public:
    // Constructor to initialize default values
    Sphere() : radius(0), volume(0.0), surface_area(0.0) {}

    // Inner class Cuboid
    class Cuboid {
    private:
        int length, width, height;
        int vol, surface_area;

    public:
        // Constructor to initialize default values
        Cuboid() : length(0), width(0), height(0), vol(0), surface_area(0) {}

        // Accepting dimensions for Cuboid
        void Accept() {
            cout << "Enter the length of cuboid: ";
            cin >> length;
            cout << "Enter the width of cuboid: ";
            cin >> width;
            cout << "Enter the height of cuboid: ";
            cin >> height;
        }

        // Calculating volume of Cuboid
        void Cal_volume() {
            vol = length * width * height;
        }

        // Calculating surface area of Cuboid
        void Cal_surfacearea() {
            surface_area = 2 * (length * width + width * height + height * length);
        }

        // Displaying Cuboid details
        void Display_data() {
            cout << "Volume of Cuboid: " << vol << endl;
            cout << "Surface Area of Cuboid: " << surface_area << endl;
        }

        // Friend function declaration to access private members
        friend double addVolumes(const Sphere& s, const Cuboid& c);
    };

    // Accepting radius for Sphere
    void Accept() {
        cout << "Enter the radius of the sphere: ";
        cin >> radius;
    }

    // Calculating volume of Sphere
    void Cal_volume() {
        volume = (4.0 / 3) * 3.14 * radius * radius * radius;
    }

    // Calculating surface area of Sphere
    void Cal_surface() {
        surface_area = 4 * 3.14 * radius * radius;
    }

    // Displaying Sphere details
    void Display() {
        cout << "Volume of Sphere: " << volume << endl;
        cout << "Surface Area of Sphere: " << surface_area << endl;
    }

    // Friend function declaration to access private members
    friend double addVolumes(const Sphere& s, const Cuboid& c);
};

// Friend function definition to add the volumes of Sphere and Cuboid
double addVolumes(const Sphere& s, const Sphere::Cuboid& c) {
    return s.volume + c.vol;
}

// Main function
int main() {
    // Creating Sphere and Cuboid objects
    Sphere sphere1;
    Sphere::Cuboid cuboid1;

    // Accepting and calculating values for sphere1
    sphere1.Accept();
    sphere1.Cal_volume();
    sphere1.Cal_surface();

    // Accepting and calculating values for cuboid1
    cuboid1.Accept();
    cuboid1.Cal_volume();
    cuboid1.Cal_surfacearea();

    // Displaying the calculated details
    sphere1.Display();
    cuboid1.Display_data();

    // Adding volumes using the friend function
    double totalVolume = addVolumes(sphere1, cuboid1);
    cout << "Total Volume (Sphere + Cuboid): " << totalVolume << endl;

    return 0;
}


