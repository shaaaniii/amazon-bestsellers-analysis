/* A structure is a user defined data type that can be used to
group elements of different types into a single type.

DECLARATION OF STRUCTURES !!
SYNTAX
struct{           use of struct keyword!
char *engine;
char *fuel_type;
int fuel_tank_cap;
int seating_cap;
float city_mileage;
}car1,car2;

Declared outside the main function in the global scope.
Example
#include<stdio.h>
struct{
char *engine;
char *fuel_type;
int fuel_tank_cap;
int seating_cap;
float city_mileage;
}car1,car2;

int main()
{
    car1.engine ="DDIS 190 Engine";
    car2.engine ="1.2 L Kappa Dual VIVT";
    printf("%s\n", car1.engine);
    printf("%s\n,",car2.engine);
    return 0;
}
 Structure declaration in a local scope
  example */
  #include<stdio.h>

   struct{
       char *name;
       int salary;
       }emp1,emp2;
   int manager ()
   {
       struct {
       char name;
       int age;
       int salary;
       }manager;
       if(manager.age>30)
        manager.salary = 65000;
       else
        manager.salary = 55000;
       return manager.salary;

   }
   int main()
   {
       printf("enter the salary of the employee 1:");
       scanf("%d\n",&emp1.salary);
       printf("enter the salary of the employee 2:");
       scanf("d\n",&emp2.salary);
       printf("enter the age of manager:");
       printf("salary of the manager %d\n",manager());  // in this if we write manager.salary the code will give an error as the salary cannot be directly accessed as the struct is declared in local scope, so to get the salary we'll write the name of the function in which the structure is declared that is the local scope.
       return 0;
   }



