#include <stdio.h>
#include <stdlib.h>

// Define the structure for a node in the linked list
struct Node {
    int data;
    struct Node *next;
};

// Function to traverse and print the linked list
void linkedlisttraversal(struct Node *ptr) {
    while (ptr != NULL) {
        printf("Element: %d\n", ptr->data);
        ptr = ptr->next;
    }
}
struct Node * deleteFirst(struct Node * head){
struct Node * ptr = head;
head = head->next;
free(ptr);
return head;

}
 struct Node * deleteInbetw(struct Node * head , int index){

    struct Node * p = head;
    struct Node * q = head->next;
    for(i=0 ; i<index-1 ; i++)
    {
        p = p->next;
        q = q->next;

    }
    p->next = q->next;
    free(q);
 }
 struct Node * deleteAtLast(struct Node * head ){
struct Node * p = head;
struct Node * q = head->next;
while(q->!= NULL){
   p = p->next;
   q = q->next;
}
 p->next=NULL;
free(q);
return head;

 }
struct Node * deleteAtVal(struct Node * head , int value){
struct Node *p = head ;
struct Node *q = head->next ;
while(q->data!=value && q->!= NULL)
{
    p = p->next;
    q = q->next;
}
if(q->data == value){
    p->next = q->next
    free(q);

}
return head;



}

    
    


int main() {
    // Declare pointers to the nodes
    struct Node *head;
    struct Node *second;
    struct Node *third;

    // Allocate memory for the nodes in the heap
    head = (struct Node *)malloc(sizeof(struct Node));
    second = (struct Node *)malloc(sizeof(struct Node));
    third = (struct Node *)malloc(sizeof(struct Node));

    // Link the first and second nodes
    head->data = 4;
    head->next = second;

    // Link the second and third nodes
    second->data = 3;
    second->next = third;

    // Terminate the list at the third node
    third->data = 8;
    third->next = NULL;

    // Traverse and print the linked list
    printf("linked list before deletion");
    linkedlisttraversal(head);

    head = deleteFirst(head);
    printf("linked list after deletion");
    //head = deleteFirst(head);
    //head = deleteInbetw(head , 2);
    linkedlisttraversal(head);
     head = deleteAtLast(head);
     linkedlisttraversal(head);
     


    return 0;
}