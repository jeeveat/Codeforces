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
	while (t > 0)
	{
		string s;
		string s_cout="";
		string s_help;
		cin >> n;
		cin >> s;
		for(int i = n-1;i>=0;i--)
			if (s[i] == '0')
			{
				s_help = char(int('a')+(int(s[i-2]) - 48)*10 + int(s[i - 1]) - 49);
				s_cout = s_help+s_cout;
				i -= 2;
			}
			else
				s_cout = char(int('a') + int(s[i])-49)+s_cout ;
		t--;
		cout << s_cout << endl;
	}
	return 0;
}
