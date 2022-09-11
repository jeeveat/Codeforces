#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#define ll long long int
using namespace std;
long long gcd(long long a, long long b) {
	while (a && b)
		if (a > b) a %= b;
		else b %= a;
	return a + b;
}
int main()
{
	int t = 1;
	ll max_ = 0;
	int count = 0;
	while (t--)
	{
		ll n; cin >> n;
		std::vector<ll> my_vector_a(n);
		std::vector<ll> my_vector_b(n);
		for (int i = 0; i < n; i++)
			cin >> my_vector_a[i];
		for (int i = 0; i < n; i++)
			cin >> my_vector_b[i];

		std::map<int, std::map<int, int>> mp;
		ll d;
		int a, b;
		int gcd_;
		std::set<std::vector<int>> my_set;
		for (int i = 0; i < n; i++)
		{
			a = my_vector_a[i];
			b = my_vector_b[i];
			while (1)
			{
				gcd_ = gcd(abs(a), abs(b));
				if (gcd_ <= 1)
					break;
				else 
				{
					a /= gcd_;
					b /= gcd_;
				}
			}
			if (a < 0)
			{
				a *= -1;
				b *= -1;
			}
			if ((a == 0) && (b == 0))
				count += 1;
			auto it = my_set.find({ a, b });
			if (it != my_set.end())
			{
				mp[a][b] += 1;
				if (mp[a][b] > max_)
					max_ = mp[a][b];
			}
			else if (a != 0)
			{
				mp[a][b] = 1;
				if (mp[a][b] > max_)
					max_ = mp[a][b];
				my_set.insert({ a,b });
			}
		}
	}
	std::cout << max_ + count << std::endl;
}