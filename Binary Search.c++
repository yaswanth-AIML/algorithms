#include <iostream>
using namespace std;
void binary(int arr[],int tar,int size){
    int star=0,end=size-1;
    while(star<=end){
        int mid=(star+end)/2;
        if(tar<arr[mid]){
            end=mid-1;
        }
        if(tar>arr[mid]){
            star=mid+1;
        }
        if (tar==arr[mid]){
            return mid;
            break;
        }
        
    }
    if (tar==arr[mid]){
        cout<<"ELEMENT FOUND";
        cout<<mid;
    }
    else{
    cout<<"NOT FOUND ";
    }
}
int main(){
    int arr[]={1,2,3,4,5,6,7,8,9};
    int tar=0;
    int size=sizeof(arr)/sizeof(arr[0]);
    cout<<"Enter The Number to find:";
    cin>>tar;
    binary(arr,tar,size);
}
