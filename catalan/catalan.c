#include <stdio.h>
#include <math.h>
#include <tgmath.h>
#include <stdlib.h>

int main() {
  long double pi;
  pi=2*acosl(0);

  int n;
  for(n=0;n<13;++n){
  
  //initialize values
  int i;
  int nv,v[5],vmax;
  long double sinv[5];
  long double a,sum,dsum,th;
  if(n==0){
    puts("    3,6,6:");
    nv=3;
    v[0]=3;
    v[1]=6;
    v[2]=6;
    vmax=6;
  } else if (n==1) {
    puts("    3,8,8:");
    nv=3;
    v[0]=3;
    v[1]=8;
    v[2]=8;
    vmax=8;
  } else if (n==2) {
    puts("    3,10,10:");
    nv=3;
    v[0]=3;
    v[1]=10;
    v[2]=10;
    vmax=10;
  } else if (n==3) {
    puts("    4,6,6:");
    nv=3;
    v[0]=4;
    v[1]=6;
    v[2]=6;
    vmax=6;
  } else if (n==4) {
    puts("    5,6,6:");
    nv=3;
    v[0]=5;
    v[1]=6;
    v[2]=6;
    vmax=6;
  } else if (n==5) {
    puts("    3,4,3,4:");
    nv=4;
    v[0]=3;
    v[1]=4;
    v[2]=3;
    v[3]=4;
    vmax=4;
  } else if (n==6) {
    puts("    3,5,3,5:");
    nv=4;
    v[0]=3;
    v[1]=5;
    v[2]=3;
    v[3]=5;
    vmax=5;
  } else if (n==7) {
    puts("    4,6,8:");
    nv=3;
    v[0]=4;
    v[1]=6;
    v[2]=8;
    vmax=8;
  } else if (n==8) {
    puts("    4,6,10:");
    nv=3;
    v[0]=4;
    v[1]=6;
    v[2]=10;
    vmax=10;
  } else if (n==9) {
    puts("    4,3,4,4:");
    nv=4;
    v[0]=4;
    v[1]=3;
    v[2]=4;
    v[3]=4;
    vmax=4;
  } else if (n==10) {
    puts("    4,3,4,5:");
    nv=4;
    v[0]=4;
    v[1]=3;
    v[2]=4;
    v[3]=5;
    vmax=5;
  } else if (n==11) {
    puts("    3,3,3,3,4:");
    nv=5;
    v[0]=3;
    v[1]=3;
    v[2]=3;
    v[3]=3;
    v[4]=4;
    vmax=4;
  } else if (n==12) {
    puts("    3,3,3,3,5:");
    nv=5;
    v[0]=3;
    v[1]=3;
    v[2]=3;
    v[3]=3;
    v[4]=5;
    vmax=5;
  }
  for(i=0;i<nv;++i){
    sinv[i]=sinl(pi*(0.5-1./v[i]));
  }
  a=0.999/sinl(pi*(0.5-1./vmax));
  
  //find bend angle
  sum=1;
  while(fabs(sum)>1.e-10){
    sum=0;
    dsum=0;
    for(i=0;i<nv;++i){
      th=asinl(sinv[i]*a);
      sum+=th;
      dsum+=sinv[i]/cosl(th);
    }
    sum*=2/pi;
    dsum*=2/pi;
    sum-=2;
    a-=sum/dsum;
  }

  //coordinates of midpoints
  long double x[10];
  th=-asinl(a*sinv[0]);
  for(i=0;i<nv;++i){
    x[2*i]=0.5*cosl(th)/a;
    x[2*i+1]=0.5*sinl(th)/a;
    th+=2.*asinl(a*sinv[i]);
  }

  //coordinates of new faces
  long double y[10];
  sum=x[0]*x[2*nv-1]-x[1]*x[2*nv-2];
  y[0]=(x[2*nv-1]-x[1])/a/a/sum/4.;
  y[1]=(x[0]-x[2*nv-2])/a/a/sum/4.;
  for(i=1;i<nv;i++){
    sum=x[2*i]*x[2*i-1]-x[2*i+1]*x[2*i-2];
    y[2*i]=(x[2*i-1]-x[2*i+1])/a/a/sum/4.;
    y[2*i+1]=(x[2*i]-x[2*i-2])/a/a/sum/4.;
  }

  //distances and angles
  long double r1,r2;
  int j,k;
  j=1;
  k=2;
  for(i=0;i<nv;++i){
    r1=sqrtl((y[2*i]-y[2*j])*(y[2*i]-y[2*j])+(y[2*i+1]-y[2*j+1])*(y[2*i+1]-y[2*j+1]));
    r2=sqrtl((y[2*k]-y[2*j])*(y[2*k]-y[2*j])+(y[2*k+1]-y[2*j+1])*(y[2*k+1]-y[2*j+1]));
    th=acosl(((y[2*i]-y[2*j])*(y[2*k]-y[2*j])+(y[2*i+1]-y[2*j+1])*(y[2*k+1]-y[2*j+1]))/r1/r2);
    printf("%Lf %Lf\n",r1,th*180./pi);
    j=k;
    k++;
    if(k==nv) k=0;
  }
  /*
  printf("#%Lf\n",0.5/a);
  for(i=0;i<nv;++i){
    printf("%Lf %Lf %i\n",x[2*i],x[2*i+1],1);
  }
  for(i=0;i<nv;++i){
    printf("%Lf %Lf %i\n",y[2*i],y[2*i+1],2);
  }
  */
  puts("");
  }
  
  return 0;
}
