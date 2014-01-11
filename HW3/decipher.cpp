#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

int main()
{
    ifstream input( "secret.txt" ), pKey( "private_key.txt" );
    ofstream output( "message.txt" );
    
    unsigned long long int secret, plain, N, d, D[ 64 ] = {}, n[ 64 ]; 
    char message[ 4 ];
    
    pKey >> N >> d;
    
    for( int i = 0; i < 64; i++ )
    {
        D[ i ] = d % 2;
        d /= 2;
    }
    
    while( !input.eof() )
    {
        input >> secret;
        plain = 1;
        n[ 0 ] = secret % N;
        
        for( int i = 1; i < 64; i++ )
            n[ i ] = n[ i - 1 ] * n[ i - 1 ] % N;
            
        for( int j = 0; j < 64; j++ )
            if( D[ j ] == 1 )
            {
                plain *= n[ j ];
                plain %= N;
            }//end if
            
        plain /= 2;
        
        message[ 0 ] = plain / pow( 2.0, 24.0 ); plain -= message[ 0 ] * pow( 2.0, 24.0 );
        message[ 1 ] = plain / pow( 2.0, 16.0 ); plain -= message[ 1 ] * pow( 2.0, 16.0 );
        message[ 2 ] = plain / pow( 2.0, 8.0 ); plain -= message[ 2 ] * pow( 2.0, 8.0 );
        message[ 3 ] = plain;
        
        for( int k = 0; k < 4; k++ )
            output << message[ k ];
    }//end while
}
