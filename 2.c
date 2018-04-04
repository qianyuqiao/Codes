#include<stdlib.h>
#include<stdio.h>
void populate_array(int * array, size_t arraysize,int (*getNextValue)(void))
{
    for(size_t i=0;i<arraysize;i++)
    array[i]=getNextValue();
    }

int getNextValue(void){
    return rand()%100; }

int main(){
int myarray[10];
populate_array(myarray,10,getNextValue);
for(int i=0;i<10;i++)
{printf("the number: %d\n",myarray[i]);}
    return 0;
}
