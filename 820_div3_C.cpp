#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include <cstdlib>
#define ll long long int
using namespace std;
int main()
{
	int t = 1;
	cin >> t;
	int n;
	char elem;
	while (t > 0)
	{
		std::vector<pair<int,int>> my_vector;
		std::vector<int> mys;
		string s;
		cin >> s;
		for (int i = 0; i < s.size();
			i++)
		{
			elem = s[i];
			int number = int(s[i]) - int('a');
			my_vector.push_back({ number,i });
		}
		std::stable_sort(my_vector.begin(),
			my_vector.end());

		auto my_iter_begin = std::find_if(my_vector.begin(),
			my_vector.end(), [s](auto& p) {return p.second == 0; });

		auto my_iter_end = std::find_if(my_vector.begin(),
			my_vector.end(), [s](auto& p) {return p.second == s.size() - 1; });

		ll cost = 0;
		ll pred = -1;
		ll k = 1;
		bool flag = false;
		if (my_iter_begin > my_iter_end)
		{
			swap(my_iter_begin, my_iter_end);

			auto help_begin = my_iter_begin;
			auto help_end = my_iter_end;

			ll help = (*my_iter_begin).first;
			while (my_iter_begin >= my_vector.begin())
			{
				if (help != (*my_iter_begin).first)
				{
					my_iter_begin++;
					break;
				}
				if (my_iter_begin != my_vector.begin())
					my_iter_begin--;
				else
					break;
			}

			help = (*my_iter_end).first;
			while (my_iter_end < my_vector.end())
			{
				if (help != (*my_iter_end).first)
				{
					my_iter_end--;
					break;
				}
				if (my_iter_end != my_vector.end()-1)
					my_iter_end++;
				else
					break;
			}
			swap(*help_begin, *my_iter_begin);
			swap(*help_end, *my_iter_end);
			flag = true;
		}
		int m = abs(std::distance(my_iter_begin, my_iter_end)) + 1;

		for (auto iElement = my_iter_begin; ; iElement++)
		{
			mys.push_back((*iElement).second + 1);
			if (pred!=-1)
				cost += abs((*iElement).first - pred);
			pred = (*iElement).first;
			if (iElement == my_iter_end)
				break;
		}

		if (flag)
			reverse(mys.begin(), mys.end());

		cout << cost <<" "<< m << endl;
		for (auto elem : mys)
			cout << elem << " ";
		cout << endl;
		t--;
		}
		
	return 0;
}