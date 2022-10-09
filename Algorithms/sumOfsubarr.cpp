#include <iostream>
using namespace std;

//using max variable , complexity  can brought down to O(n)

int sum_subarray(int arr[],int n){
    int res=arr[0];
for(int i=0;i<n;i++){
    int curr=0;
    for(int j=i;j<n;j++){
      curr+=arr[j];
      res=max(curr,res);
    }
}
return res;


}


int main(){
int arr[7]={2,3,-8,7,-1,2,3};
int n =sizeof(arr)/4;
cout<<sum_subarray(arr,n);

}