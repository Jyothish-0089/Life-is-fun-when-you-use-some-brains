#include<stdio.h>
int main(){
	int len;
	printf("Length of Array: ");
	scanf("%d",&len);
	int array[len],i;
	for(i=0;i<len;i++){
		printf("Element: ");
		scanf("%d",&array[i]);
	}
	printf("Array: ");
	for(i=0;i<len;i++){
		printf("%d ",array[i]);
	}
	i=0;
	int j=1,temp;
	while(j<len){
		if(array[i]>array[j]){
			temp = array[j];
			array[j]=array[i];
			array[i]=temp;
			if(i>0){
				i--;
			    j--;
			}
     	}
		else{
			i++;
			j++;
		}	
	}
	printf("\nSorted Array: ");
	for(i=0;i<len;i++){
		printf("%d ",array[i]);
	}
}
