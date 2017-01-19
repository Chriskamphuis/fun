#include <stdio.h>
#include <stdlib.h>

struct int_node{
	int x;
	struct int_node* next;
};

void free_list(struct int_node* linked_list)
{
	while(linked_list != 0){
		struct int_node *next = linked_list->next;
		free(linked_list);
		linked_list = next;
	}
	return;
}

void print_list(struct int_node* linked_list){
  	struct int_node* iterator = linked_list;
	while(iterator->next != 0){
		printf("%i ", iterator->x);
		iterator = iterator->next;
	}
	printf("%i\n", iterator->x);
	return;
}

void add_element(struct int_node* linked_list, int element){
	while(linked_list->next != 0){
		struct int_node *next = linked_list->next;
		linked_list = next;
	}
	linked_list->next = malloc(sizeof(struct int_node));
	linked_list->next->next = 0;
	linked_list->next->x = element;
	return;
}

void insert_node(struct int_node* after_me, struct int_node* new_node){
	new_node->next = after_me->next;
	after_me->next = new_node;
	return;
}

void delete_after(struct int_node* after_me){
  	struct int_node* temp = after_me->next;
	after_me->next = temp->next;
	free(temp);
	return;
}

struct int_node* find_node_before(struct int_node* node, int target){
  	if(node == NULL) return NULL;
	while(node->next != NULL){
		if(node->next->x == target) return node;
		node = node->next;
	}
	return NULL;
}

struct int_node* find_node(struct int_node* node, int target){
  	while(node != NULL){
		if(node->x == target) return node;
		node = node->next;
	}
  	return NULL;
}

struct int_node* empty_list(void){
	return malloc(sizeof(struct int_node));
}

int main(void){
	struct int_node* root = empty_list();  
	root->x = 0;
	root->next = 0;
	int i;
	for(i=0; i<100; i++) add_element(root, i%20);	
	struct int_node* temp = find_node(root, 12);
	delete_after(temp);
	print_list(root);
	return 0;
}
