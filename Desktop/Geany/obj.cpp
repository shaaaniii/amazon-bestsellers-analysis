#include<iostream>
using namespace std;
  
  class student
  {
	  private:
	  int marks;
	  int roll_no;
	  
	  char name ;
	  char gender;
	  
	  public:
	  void accept_data(){
	  cout<<"enter the name :";
	  cin>>name;
	  cout<<"enter the gender :";
	  cin>>gender;
	  cout<<"enter the roll no :";
	  cin>>roll_no;
	  cout<<"enter the marks:";
	  cin>>marks;
  }
 void display_data(){
	 cout<<"the name is:"<<name<<endl;
	 cout<<"the gender is:"<<gender<<endl;
	 cout<<"the roll no is:"<<roll_no<<endl;
	 cout<<"the marks is:"<<marks<<endl;
 
 
 }
};

int main(){
	student stud1,stud2;
	stud1.accept_data();
	stud2.accept_data();
	stud1.display_data();
	stud2.display_data();
	return 0;
}
	  
