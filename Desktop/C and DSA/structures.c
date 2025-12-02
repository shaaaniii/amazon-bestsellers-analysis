#include<stdio.h>
struct employee{
    int code;
    float salary;
    char name[10];

};

int main(){
    struct employee emp1, emp2;
    emp1.code = 101;
    emp1.salary = 5000.0;
    strcpy(emp1.name, "Rahul");
    emp2.code = 102;
    emp2.salary = 6000.0;
    strcpy(emp2.name, "Rohan");
    printf("Employee 1 details:\n");
    printf("Code: %d\n", emp1.code);
    printf("Salary: %.2f\n", emp1.salary);
    
}