#include <stdio.h>
#include <math.h>
#include <tgmath.h>
#include <stdlib.h>

int main() {
  int a,b,f,bmax;
  long double y,al,bl,fl;

  for(a=1;a<5;++a){
    al=(long double) a;
    bmax=2*a;
    if(bmax>5) bmax=5;
    for(b=1;b<bmax;++b){
      bl=(long double) b;
      for(f=0;f<a;++f){
	fl=(long double) f;
	y=0.25*(al-fl)*sqrtl(bl/(2.*al-bl));
	printf("%1i %1i %1i %Lf %Lf\n",a,b,f,y,y*11./17.);
      }
    }
  }
  
  return 0;
}
