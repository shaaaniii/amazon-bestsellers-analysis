#include<stdio.h>
#include<stdlib.h>

struct myarray{
    int total_size;
    int used_size;
    int *ptr;
};
void create_array(struct myarray * a , int tSize ,int uSize){
    a-> total_size = tSize;
    a->used_size = uSize;
    a->ptr = (int*)malloc(tSize*sizeof(int));
}

void show(struct myarray *a){
    for(int i = 0; i < a->used_size; i++){
        printf("%d \n", (a->ptr)[i]);

    }
}

void setVal(struct myarray *a){
    int n;

    for(int i = 0; i < a->used_size; i++)
    {
        printf("enter element %d  " ,i);
        scanf("%d",&n);
        (a->ptr)[i] = n;

    }
}
int main(){
    struct myarray marks;
    create_array(&marks,100,20);
    setVal(&marks);
    show(&marks);



    return 0;
    
}