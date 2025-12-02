#include<iostream>
using namespace std;
int main(){
	int marks;
	cout<<"enter your marks";
	cin>>marks;
	if(marks<25){
		cout<<"grade F";
	}
	else if(marks<=44){
		cout<<"grade E";
	}
	else if(marks<=49){
		cout<<"grade D";
	}
	else if(marks<=59){
		cout<<"grade C";
	}
	else if(marks<=79){
		cout<<"grade B";
	}
	else if(marks<=100){
		cout<<"grade A";
	}
	return 0;
}
