#include<stdio.h>
#include<stdlib.h>

int main(){
double a=2.0;
double* a1= &a;
double ** m;
m=(double**)(malloc((size_t)10*sizeof(double*)));
*m=a1;
printf("%f\n",**m);
return 0;
}
