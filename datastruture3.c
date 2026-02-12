#include<stdio.h>
int main()
{
    int array[50],i,size,pos=0;
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
    int num;
    printf("enter the number to found");
    scanf("%d",&num);
    for(i=0;i<size;i++)
    {
        if(num==array[i]);
        {
           pos=i;
           printf("%d",i);
           
        }
            
    }
    if(pos==0)
    printf("number not found");
    else{
        printf("number is found");
    }

}