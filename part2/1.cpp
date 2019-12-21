#include <bits/stdc++.h>
using namespace std;
int main()
{
    int a[2][2] = {{53947,56211},{19385,43159}};
    for(int i=0;i<2;i++){
        int s=0,olds=1,t=1,oldt=0,r=a[i][0],oldr=a[i][1],q,t1;
        while(r!=0){
            q=oldr/r;
            t1=r;
            r=oldr-(q*r);
            oldr = t1;
            t1=s;
            s = olds-(q*s);
            olds = t1;
            t1 = t;
            t=oldt-(q*t);
            oldt=t1;
        }
        if(oldt<0){
            oldt+=a[i][1];
        }
        cout<<"Multiplicative inverse of "<<a[i][0]<<"^-1mod"<<a[i][1]<<" is "<<oldt<<endl;
    }

    return 0;
}