#include <stdio.h>
#include <stdlib.h>

// Define the structure for a node in the linked list
struct Node
{
    int data;
    struct Node *next;
};

// Function to traverse and print the linked list
void linkedlisttraversal(struct Node *ptr)
{
    while (ptr != NULL)
    {
        printf("Element: %d\n", ptr->data);
        ptr = ptr->next;
    }
}
struct Node *insertAtFirst(struct Node *head, int data)
{
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    ptr->next = head;
    ptr->data = data;
    return ptr;
}
struct Node *insertInBetween(struct Node *head, int data, int index)
{
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    struct Node *p = head;
    int i = 0;
    // this while loop states that the i is one before where we wish to insert our p
    while (i != index - 1)
    {
        p = p->next;
        i++;
    }
    ptr->data = data;
    ptr->next = p->next;
    p->next = ptr;
    return head;
}
struct Node *insertAtEnd(struct Node *head, int data)
{
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    struct Node *p = head;
    while (p->next != NULL)
    {
        p = p->next;
    }
    ptr->data = data;
    p->next = ptr;
    ptr->next = NULL;
    return head;
}
struct Node *insertAfternode(struct Node *head, struct Node *prevnode, int data)
{
    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));

    ptr->next = prevnode->next;
    prevnode->next = ptr;
}
int main()--
    // Declare pointers to the nodes
    struct Node *head;
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
    printf("linked list before insertion\n");
    linkedlisttraversal(head);
    // head = insertAtFirst(head , 56);
    // head = insertInBetween(head , 56 , 1);
    // head = insertAtEnd(head , 78 );
    printf("linked list after insertion\n");
    head = insertAfternode(head, second, 45);
    linkedlisttraversal(head);

    return 0;
}
