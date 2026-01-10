#include <stdio.h>
#include <stdlib.h>

typedef struct Node
{
    int data;
    struct Node *next;
} Node;

int main(void)
{
    Node *head = NULL;
    Node *second = NULL;
    Node *third = NULL;

    // allocate some nodes in the heap
    head = (Node *)malloc(sizeof(Node));
    second = (Node *)malloc(sizeof(Node));
    third = (Node *)malloc(sizeof(Node));

    // link nodes together and assign data
    head->data = 1;
    head->next = second;

    second->data = 2;
    second->next = third;

    third->data = 3;
    third->next = NULL;

    // print the list
    Node *current = head;
    while (current != NULL)
    {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");

    // free allocated memory
    free(third);
    free(second);
    free(head);

    return 0;
}