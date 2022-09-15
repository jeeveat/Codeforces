#include<iostream>
#include<vector>
#include<algorithm>
#define ll long long int
using namespace std;
int main()
{
	int t = 1;
	cin >> t;
	ll a, b, c;
	ll first, second;
	while (t > 0)
	{
		cin >> a >> b >> c;
		first = abs(1 - a);
		second = abs(b - c) + abs(c - 1);
		if (first == second)
			cout << 3 << endl;
		else if (first < second)
			cout << 1 << endl;
		else
			cout << 2 << endl;
		t--;
	}
	return 0;
}
