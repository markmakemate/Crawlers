#ifndef KMP_ALGORITHM_H
#define KMP_ALGORITHM_H
#include<iostream>
#include<cstring>
using namespace std;
class KMP{
public:
    int KMP_Algorithm(string Pattern,string Text);
    int* Compute_Prefix_Function(string Pattern);
};
int KMP::KMP_Algorithm(string Pattern,string Text){
    int n=Text.size();
    int m=Pattern.size();
    int* pi=new int[m];
    int Position=-1;
    pi=Compute_Prefix_Function(Pattern);
    int q=0;
    for(int i=0;i<n;i++){
        while(q>=0&&Pattern.at(q+1)!=Text.at(i)){
            q=*(pi+q);
        }
        if(q==m){
            q=*(pi+q);
            Position=i;
            break;
        }
        else if(Pattern.at(q+1)==Text.at(i)){
            q=q+1;
        }
    }
    return Position;
}
int* KMP::Compute_Prefix_Function(string Pattern){
    int m=Pattern.size();
    int* pi=new int[m];
    pi[0]=0;
    int k=0;
    for(int i=1;i<m;i++){
        while(k>=0&&Pattern.at(k+1)!=Pattern.at(i)){
            k=pi[k];
        }
        if(Pattern.at(k+1)==Pattern.at(i)){
            k++;
        }
        pi[i]=k;
    }
    return pi;
}

extern "C"{
    KMP kmp;
    int kmp_algorithm(string pattern,string text){
        return kmp.KMP_Algorithm(pattern,text);
    }
    int* compute_prefix_function(string pattern){
        return kmp.Compute_Prefix_Function(pattern);
    }
}
#endif