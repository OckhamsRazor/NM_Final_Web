#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

int main()
{
    ifstream input( "plain.txt" ), NED( "public_key.txt" );
    ofstream output( "secret.txt" );
    int length, remainder;
    unsigned long long int plain, secret = 1, N, e, d, n[ 64 ] = {}, E[ 64 ] = {};
    string message;

    getline( input, message );
    NED >> N >> e;
    
    for( int i = 0; i < 64; i++ )
    {
        E[ i ] = e % 2;
        e /= 2;
    }

    length = message.length();
    remainder = length % 4;

    for( int i = 0; i < length - remainder; i+=4 )
    {
         secret = 1;
         plain = ( message[ i ] * pow( 2.0, 24.0 ) 
                 + message[ i + 1 ] * pow( 2.0, 16.0 )
                 + message[ i + 2 ] * pow( 2.0, 8.0 )
                 + message[ i + 3 ] ) * 2;
        
        n[ 0 ] = plain % N;
        for( int j = 1; j < 64; j++ )
            n[ j ] = n[ j - 1 ] * n[ j - 1 ] % N;
            
        for( int j = 0; j < 64; j++ )
            if( E[ j ] == 1 )
            {
                secret *= n[ j ];
                secret %= N;
            }//end if
            
        output << secret;
        if( i != length - 4 )
           output << " ";
    }//end outer for
    
    if( remainder != 0 )
    {
        secret = 1;
        plain = 0;
        for( int i = 0; i < remainder; i++ )
            plain += ( message[ length - remainder + i ] * pow( 2.0, 24.0 - 8.0 * i )); 
        plain *= 2;
        
        n[ 0 ] = plain % N;
        for( int j = 1; j < 64; j++ )
            n[ j ] = n[ j - 1 ] * n[ j - 1 ] % N;
            
        for( int j = 0; j < 64; j++ )
            if( E[ j ] == 1 )
            {
                secret *= n[ j ];
                secret %= N;
            }//end if
        output << secret;
    }//end if
}//end main
