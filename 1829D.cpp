#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include <cstdlib>
#define ll long long int
using namespace std;
 
int main() {
	int t; cin >> t;
	while (t--) {
		int n;
		cin >> n;
 
		vector<ll> x(n);
		ll y;
		vector<ll> my_vector(n);
 
		for (int i = 0; i < n; i++)
			cin >> x[i];
 
		for (int i = 0; i < n; i++)
		{
			cin >> y;
			my_vector[i] = y-x[i];
		}
 
		std::sort(my_vector.begin(), my_vector.end());
		std::reverse(my_vector.begin(), my_vector.end());
		auto l_iter = my_vector.begin();
		auto r_iter = my_vector.end()-1;
		size_t count = 0;
		ll sum = 0;
		while (l_iter < r_iter)
		{	
			sum = *l_iter + *r_iter;
			if (sum >=0)
			{
				count++;
				sum = 0;
				r_iter--;
				l_iter++;
			}
			else
				r_iter--;
		}
		std::cout << count << endl;
 
	}
	return 0;
}
