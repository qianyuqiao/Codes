#include<stdio.h>
int max(int x,int y){
    return x>y?x:y;
    }

int main(){
int (*p)(int,int)=&max;
int a,b,c;
printf("please input 3 numbers\n");
scanf("%d %d %d",&a,&b,&c);
int d=p(p(a,b),c);
printf("the max number is %d\n",d);
return 0;
    }
