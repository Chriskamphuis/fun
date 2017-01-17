#include <stdio.h>
#include <stdlib.h>

struct int_node{
	int x;
	struct int_node *next;
};

void free_linked_list(struct int_node *linked_list)
{
	while (linked_list != 0){
		struct int_node *next = linked_list->next;
		free(linked_list);
		linked_list = next;
	}
}


int main(void){
	struct int_node *root;	
	root = malloc(sizeof(struct int_node));  
	root->next = 0;   
	root->x = 12;
	printf("%i\n", root->x);
	return 0;
}
