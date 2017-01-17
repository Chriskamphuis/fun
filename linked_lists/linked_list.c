#include <stdio.h>
#include <stdlib.h>

struct node{
	  int x;
		struct node *next;
};

int main(){
	struct node *root;	
	root = malloc( sizeof(struct node) );  
	root->next = 0;   
	root->x = 12;
	printf("%i\n", root->x);
	return 0;
}
