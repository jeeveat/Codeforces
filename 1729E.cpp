#include<iostream>
#include"math.h"
#include<algorithm>
#define ll long long
using namespace std;

int main()
{
	ll a=1, b=3, n1,n2;
	ll number=0;
	ll max_ = 2;
	for (int i = 0; i < 25; i++)
	{
		cout << "? " << 1 << " " << b << endl;
		cin >> n1;
		
		cout << "? " << b << " " << 1 << endl;
		cin >> n2;

		if (n1 != n2)
		{
			number = n1 + n2;
			break;
		}
		if (n1 == -1)
		{
			number = b - 1;
			break;
		}
		b++;
	}
	cout << "! " << number << endl;
	return 0;
}