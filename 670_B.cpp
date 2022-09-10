#include<bits/stdc++.h>
#define ll long long int
using namespace std;
int main()
{
	int t; cin >> t;
	while (t--)
	{
		ll n; cin >> n;
		ll a[n];
		for (auto& i : a)
			cin >> i;
		sort(a, a + n);
		cout << max({ a[0] * a[1] * a[n - 1] * a[n - 2] * a[n - 3],a[0] * a[1] * a[2] * a[3] * a[n - 1],a[n - 5] * a[n - 4] * a[n - 1] * a[n - 2] * a[n - 3] }) << "\n";
	}
}