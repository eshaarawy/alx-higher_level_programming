#include "lists.h"

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 *
 * Return: 1 if it's a palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	int arr[1024];
        int i = 0, j = 0;
	listint_t *current = *head;

	if (*head == NULL)
		return 1;
	while (current != NULL)
	{
		arr[i] = current->n;
		current = current->next;
		i++;
	}
	i--;
	while (j <= i)
	{
		if (arr[j] != arr[i])
			return 0;
		j++;
		i--;
	}
	return 1;
}

