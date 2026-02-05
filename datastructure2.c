#include<stdio.h>
int main()
{
    int array[100],size,del,i;
    printf("enter the size of the array");
    scanf("%d",&size);
    for(i=0;i<size;i++)
    {
        printf("enter the %d ",i);
        scanf("%d",&array[i]);
    } 
    for( i=0;i<size;i++)
    {
       printf("%d \n",array[i]);
    }
    printf("enter the number where to delete that data");
    scanf("%d",&del);
    for(i=del-1;i<size-1;i++)
    {
        array[i]=array[i+1];
    }
    size--;
    for(i=0;i<size;i++)
    {
        printf("%d",array[i]);
    }
}