#include <cstdio>
#include <stack>
#include <queue>
#include <cmath>
#include <vector>
#include <cstring>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;
#define CLR(a,b) memset(a,b,sizeof(a))
#define INF 0x3f3f3f3f
#define LL long long
#define fi first
#define se second
int main()
{
	int n;
	string a,b;
	vector<pair<string,string> > d;
	scanf ("%d",&n);
	while (n--)
	{
		cin >> a >> b;
		bool flag = false;
		for (int i = 0 ; i < d.size() ; i++)
		{
			if (d[i].se == a)
			{
				d[i].se = b;
				flag = true;
			}
		}
		if (!flag)
			d.push_back(make_pair(a,b));
	}
	printf ("%d\n",d.size());
	for (int i = 0 ; i < d.size() ; i++)
		cout << d[i].fi + ' ' + d[i].se << endl;
	return 0;
}
