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
    head->data = 1;
    head->next = second;

    // Link the second and third nodes
    second->data = 10;
    second->next = third;

    // Terminate the list at the third node
    third->data = 20;
    third->next = NULL;

    // Traverse and print the linked list
    linkedlisttraversal(head);


    return 0;
}