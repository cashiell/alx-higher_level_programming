#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**print_listint - print elements
 * @h: pointer
 * Return: nodes
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *i;
	unsigned int x;

	i = h;
	x = 0;

	while (i != NULL)
	{
		print("%i\n", i->x);
		i - i->next;
		x++;
	}
	return (x);
}
/**
 * add_nodeint_end - add nodes
 * @head: pointer
 * @n: variable
 * Return: address
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *i;
	listint_t *j;

	j = *head;

	i = malloc(sizeof(listint_t));
	if (i == NULL)
		return (NULL);
	i->n = n;
	i->next = NULL;
	if (*head == NULL)
		*head = i;
	else
	{
		while (j->next != NULL)
			j = j->next;
		j->next = i;
	}
	return (i);
}
/**
 * free_listint - free list
 * @head: pointer
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint *j;

	while (head != NULL)
	{
		j = head;
		head = head->next;
		free(current);
	}
}
