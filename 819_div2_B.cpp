#include <iostream>
#include <vector>
using namespace std;

int main()
{	
	int p;
	cin >> p;
	int n, m;
	for (int t = 0; t < p; t++)
	{
		cin >> n >> m;
		vector<int> my_vector(n);

		if (n > m)
			cout << ("NO") << endl;
		else
		if (m % 2 == 0 )
		{
			cout << ("YES") << endl;
			if (n % 2 == 0) 
			{
				for (int i = 0; i < n - 2; i++)
					cout << 1<<" ";
				cout << (m - (n - 2))/2<<" "<< (m - (n - 2)) / 2 << endl;
			}
			else
			{
				for (int i = 0; i < n - 1; i++)
					cout << 1 << " ";
				cout << (m - (n - 1)) << endl;
			}
		}
		else
		{
			if (n % 2 == 0)
				cout << ("NO") << endl;
			else
			{
				cout << ("YES") << endl;
				for (int i = 0; i < n - 1; i++)
					cout << 1 << " ";
				cout << (m - (n - 1)) << endl;
			}

		}
	}
}