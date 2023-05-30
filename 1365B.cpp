#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <iomanip>
#include <numeric> 
#define ll long long

int firstDel(ll n)
{
    for (int i = 2; i<=pow(n,0.5)+1;i++)
    {
        if (n % i == 0)
            return i;
    }
    return 1;
}

void solve()
{
    ll n;
    std::cin >> n;

    int k = firstDel(n);

    if(k>1)
        std::cout << n / k << " " << n - n / k << std::endl;
    else
        std::cout << 1 << " " << n-1 << std::endl;

}

int main() 
{
    int t;
    std::cin >> t;
    while (t--)
        solve();
    return 0;
}
