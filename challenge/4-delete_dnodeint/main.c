#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * delete_all_nodes - Deletes all nodes in a doubly linked list.
 * @head: Double pointer to the head of the doubly linked list.
 *
 * This function iteratively deletes all nodes in the doubly linked list
 * starting from the head, and prints the list after each deletion.
 */
void delete_all_nodes(dlistint_t **head)
{
	while (*head != NULL)
	{
		delete_dnodeint_at_index(head, 0);
		print_dlistint(*head);
		printf("-----------------\n");
	}
}

int main(void)
{
	dlistint_t *head;

	head = NULL;
	add_dnodeint_end(&head, 0);
	add_dnodeint_end(&head, 1);
	add_dnodeint_end(&head, 2);
	add_dnodeint_end(&head, 3);
	add_dnodeint_end(&head, 4);
	add_dnodeint_end(&head, 98);
	add_dnodeint_end(&head, 402);
	add_dnodeint_end(&head, 1024);
	print_dlistint(head);
	printf("-----------------\n");
	delete_dnodeint_at_index(&head, 5);
	print_dlistint(head);
	printf("-----------------\n");
	delete_all_nodes(&head);
	free_dlistint(head);
	return (0);
}
