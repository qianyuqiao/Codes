#include<stdio.h>
int main()
{

double* a[10];
double**  p= a;

double a01=2.0;
double* a1=&a01;

a[0]=a1;
printf("%f\n",**p);

return 0;

}
