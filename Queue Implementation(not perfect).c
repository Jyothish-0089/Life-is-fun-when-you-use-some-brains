#include <stdio.h>
int main(){
	int max,num,rear=-1,front=0,choice,i;
	printf("Enter the length of queue: ");
	scanf("%d",&max);
	int queue[max];
	while(choice!=4){
		printf("1.ENQUEUE    2.DEQUEUE    \n3.DISPLAY    4.EXIT\nChoice: ");
		scanf("%d",&choice);
		if(choice==1){
			rear++;
			if(rear>=max){
				printf("\n---Overflow!!---\n\n");
				rear--;
		    }
			else{
				printf("Enqueue Element: ");
				scanf("%d",&queue[rear]);
			}
		}
		if(choice==2){
			if(front==max){
				printf("\nUnderflow!!\n\n");
			}
			else{
				printf("Element Dequeued\n");
				front++;
			}
		}
		if(choice==3){
			printf("Array: ");
			for(i=front;i<rear+1;i++){
				printf("%d ",queue[i]);
			}
			printf("\n");
		}
	}
}
