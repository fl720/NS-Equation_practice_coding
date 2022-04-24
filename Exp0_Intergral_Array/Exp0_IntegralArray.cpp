#include <iostream>
#include <vector> 

using namespace std ;

// In = 1/n - 5In-1

int main(){
    
    vector<float> I(101,0) ;

    I[100] = 1 ; 

    for( int i = 99 ; i >= 0 ; i-- )
    {
        I[i] = 0.2/(i+1) - I[i+1]/5 ; 
    }
    
    cout << I[0] <<endl; // should be 0.1823215567939546

    return 0; 
}

