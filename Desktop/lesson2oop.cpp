#include<bits/stdc++.h>
using namespace std;

class animal
{
private:
    string a , b , c;

public:
    void enterdata(){
    cout<<"enter the animal name in a:";
    cin>>a;
    cout<<"enter the animal name in b:";
    cin>>b;
    cout<<"enter the animal name in c:";
    cin>>c;



    }
    void displaydata(){
    cout<<"animal a:"<<a<<endl;
    cout<<"animal b:"<<b<<endl;
    cout<<"animal c:"<<c<<endl;

    }
};

int main(){
animal vice;
vice.enterdata();
vice.displaydata();
return 0;
}
