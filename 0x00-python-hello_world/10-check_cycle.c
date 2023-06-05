#include "lists.h"
/**
 * check_cycle - write a function that checks if a singly linked
 * list has a cycle in it
 * @list: pointer
 * Return: 0
 */
int check_cycle(listint_t *list)
{
	listint_t *i, *j;

	if (list == NULL || list->next == NULL)
		return (0);
	i = list;
	j = i->next;
	while (i != NULL && j->next != NULL && j->next->next != NULL)
	{
		if (i == j)
			return (1);
		i = i->next;
		j = j->next->next;
	}
	return (0);
}
