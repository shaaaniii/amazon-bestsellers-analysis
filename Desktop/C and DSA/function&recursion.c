/*#include<stdio.h>
void display();
 
 int main(){
    int a;
    display();
    return 0;
 }
 void display(){
    printf("hi i'm display");

 }*/
 #include<stdio.h>
 #include<math.h>
 int factorial (int x);

int main(){
int x = 5;
printf("the factorial of %d is %d",x ,factorial(x));

}
int factorial (int x){
   if(x==1 || x==0){
   return 1;
   }
   else{
   return x * factorial(x-1);
   }




