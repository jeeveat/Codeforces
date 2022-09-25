#include<iostream>
#include"math.h"
#include<algorithm>
#include<string>
#include<map>
#include<vector>
#define ll long long
using namespace std;


void solve()
{
	ll n, c;
	
	cin >> n >> c;

	vector<int> my_vec(n);

	for (int i = 0; i < n; i++)
		cin >> my_vec[i];

	sort(my_vec.begin(), my_vec.end());

	ll sum = 0;
	ll count = 1;
	ll pred_elem = my_vec[0];
	if (n == 1)
		sum = 1;
	for (int i = 1; i < n; i++)
	{
		if (pred_elem == my_vec[i])
			count++;
		else
		{
			sum += min(c,count);
			count = 1;
		}
		pred_elem = my_vec[i];
		if (i == n - 1)
			sum += min(count , c);
	}
	cout << sum << endl;

}

int main()
{
	int t;
	cin >> t;
	while (t--)
		solve();
	return 0;
}