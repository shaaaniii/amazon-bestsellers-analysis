#include<iostream>
using namespace std;
class time
{
private:

        int hr,mins,sec;

public:
        void Accept_time()
        {


        cout<<"enter the hour :";
        cin>>hr;
        cout<<"enter the minutes :";
        cin>>mins;
        cout<<"enter the seconds :";
        cin>>sec;

    }
void Display_time()
{
    cout<<hr<<":"<<mins<<":"<<sec<<endl;

}
time add_time(time ob)
{

    time tmp;
    tmp.hr=hr+ob.hr;
    tmp.mins=mins+ob.mins;
    tmp.sec=sec+ob.sec;

if(tmp.sec>=60){
    tmp.mins++;
    tmp.sec-=60;
}
if(tmp.mins>=60){
    tmp.hr++;
    tmp.mins-=60;
}
 return tmp;
}

};
int main()
{

time time1,time2,time3;
time1.Accept_time();
time2.Accept_time();
time3=time1.add_time(time2);
time1.Display_time();
time2.Display_time();
time3.Display_time();
return 0;
}
