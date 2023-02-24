#include<stdio.h>
int main(){
	int len,choice,i;
	printf("Length of Stack: ");
	scanf("%d",&len);
	int stack[len],top=0;
	while(choice!=4){
		printf("\n1.PUSH    2.POP\n3.PEEK    4.EXIT\n");
		scanf("%d",&choice);
		if(choice==1){
			if(top==len){
				printf("\nOverflow!\n");
			}
			else{
				printf("Enter Element: ");
			    scanf("%d",&stack[top]);
			    top++;
			}
		}
		if(choice==2){
			printf("Element %d Popped",stack[top-1]);
			top--;
		}
		if(choice==3){
			printf("Stack: {");
			for(i=0;i<top;i++){
				printf("%d ",stack[i]);
			}
			printf("}");
		}
	}
}
