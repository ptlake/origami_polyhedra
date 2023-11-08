#include <stdio.h>
#include <math.h>
#include <tgmath.h>
#include <stdlib.h>

int main() {
  int a,b,c,bmax;
  long double al,bl,cl,th,phi,thp,pi;

  pi=2.*acosl(0.);

  for(a=1;a<5;++a){
    al=(long double) a;
    bmax=2*a;
    if(bmax>5) bmax=5;
    for(b=1;b<bmax;++b){
      bl=(long double) b;

      phi=0.5*acosl(1.-bl/al);
      thp=atanl(0.5*al*tanl(phi));
      if(thp<0) thp*=-1;
      printf("%1i %1i %1i %Lf\n",a,b,0,180-thp/pi*360.);
      for(c=1;c<4;++c){
	cl=(long double) c;
	th=0.5*(thp+acosl((1.-0.5*cl)*cos(thp)));
	printf("%1i %1i %1i %Lf\n",a,b,c,180-th/pi*360.);
      }
    }
  }
  
  return 0;
}
