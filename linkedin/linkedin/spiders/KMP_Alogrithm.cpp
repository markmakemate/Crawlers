#include<iostream>
#include<cstring>
#include"KMP_Alogrithm.h"
using namespace std;
int main(){
    int result;
    KMP kmp;
    cout<<kmp.KMP_Algorithm("abb","abbcbd");
    cout<<endl;
    cout<<kmp.KMP_Algorithm("abc","abbcb");
    return 0;
}