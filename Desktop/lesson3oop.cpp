#include <bits/stdc++.h>
using namespace std;
class binary
{
private:
    string s;
public:
    void read();
    void check_binary();
    void ones_compliment();
    void display();

};

void binary::read()
{
    cout<<"enter a binary number"<<endl;
    cin>>s;

}
void binary::check_binary()
{
    for(int i = 0; i < s.length(); i++)
    {
        if(s.at(i)!='0'&& s.at(i)!='1')
        {
            cout<<"incorrect format"<<endl;

        }

    }
}
void binary::ones_compliment()
{
check_binary();
    for(int i = 0; i < s.length(); i++)
    {
        if(s.at(i)=='0')
        {
            s.at(i) ='1';
        }
        else
        {
            s.at(i) ='0';
        }
    }
}

void binary::display()
{
    cout<<"displaying your binary number"<<endl;
    for(int i = 0; i < s.length(); i++)
    {
        cout<<s.at(i);
    }

cout<<endl;
}

int main()
{
    binary s;
    s.read();
    //s.check_binary();
    s.display();
    s.ones_compliment();
    s.display();
    return 0;
}
