#include<iostream>
#include<vector>
/*It is going to be my favourite sum ever i had attended in guvi*/
using namespace std;
int main(){
int m;
cin>>m;
int ic=0;
int a[m+2][m+2];
for(int i=0;i<m+2;i++){
    for(int j=0;j<m+2;j++){
        a[i][j]=0;
    }
}
for(int i=1;i<=m;i++){
    for(int j=1;j<=m;j++){
        cin>>a[i][j];
    }
}
for(int i=1;i<=m;i++){

    for(int j=1;j<=m;j++){
        vector<int> x,y;
        x.push_back(i-1);
        y.push_back(j-1);
        x.push_back(i-1);
        y.push_back(j);
        x.push_back(i-1);
        y.push_back(j+1);
        x.push_back(i);
        y.push_back(j-1);
        x.push_back(i);
        y.push_back(j+1);
        x.push_back(i+1);
        y.push_back(j-1);
        x.push_back(i+1);
        y.push_back(j);
        x.push_back(i+1);
        y.push_back(j+1);
        int d=0;
        for(int ii=0;ii<8;ii++){
            if(a[i][j]==1&&a[x[ii]][y[ii]]==0){
                d+=1;
            }
            else{
                break;
            }
        }
        if(d==8){
            id++;
        }
    }
}
cout<<id;
return 0;
}
