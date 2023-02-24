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
	printf("\n");
	int pass=0,j=1,temp,k;
	i=0;
	while(pass<len-1){
		while(j<len){
			if(array[i]>array[j]){
				temp = array[i];
				array[i] = array[j];
				array[j] = temp;
			}
			i++;
			j++;
	    }
	    pass++;
	    i=0;
	    j=1;
	    printf("\nPass-%d Array: ",pass);
    	for(k=0;k<len;k++){
			printf("%d ",array[k]);
	    }
	    printf("\n");
    }
}
