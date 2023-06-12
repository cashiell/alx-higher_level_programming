#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer
 *
 * Return: results
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer
 *
 * Return:  if not palindrome - 0.
 *         If a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *x, *y, *z;
	size_t size = 0, i;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	x = *head;
	while (x)
	{
		size++;
		x = x->next;
	}

	x = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		x = x->next;

	if ((size % 2) == 0 && x->n != x->next->n)
		return (0);

	x = x->next->next;
	y = reverse_listint(&x);
	z = y;

	x = *head;
	while (y)
	{
		if (x->n != y->n)
			return (0);
		x = x->next;
		y = y->next;
	}
	reverse_listint(&z);

	return (1);
}
