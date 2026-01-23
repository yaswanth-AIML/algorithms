#include<stdio.h>
int main()
{
    int arr[100],size,i=0,j=0;
    printf("enter the size of the array");
    scanf("%d",&size);
    if(size>100)
    {
        printf("array cannot be inserted");
    }
    else{
        for(i=0;i<size;i++)
        {
            printf("enter the %d element of the array :",i);
            scanf("%d", &arr[i]);
        }
        for(i=0;i<size-1;i++)
        {
            for(j=0;j<size-1;j++)
            {
                if(arr[j]>arr[j+1])
                {
                  int temp=0;
                  temp=arr[j];
                  arr[j]=arr[j+1];
                  arr[j+1]=temp;
                }
            }
        }
        for(int i=0;i<size;i++)
        {
            printf("%d",arr[i]);
        }
        
    }
}