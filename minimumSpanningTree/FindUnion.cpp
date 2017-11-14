#include <iostream>
#include <unordered_map>
using namespace std;
class Disjoint_set
{
	unordered_map<char,char> PARENT;
public:
	Disjoint_set()
	{
		char universe[] = {'a','b','c','d','e'};
		for (char x : universe)
		{
			PARENT[x] = x;
		}
		PARENT['d'] = 'b';
	}
	char Find(char item)
	{
		if (PARENT[item] ==item)
			{cout<<"found item "<<item<<endl;
			return item;}
		else
			{return Find(PARENT[item]);}
	}
	void Union(char set_1, char set_2)
	{
		PARENT[set_1] = set_2;
	}
	void printParent()//(unordered_map<char,char> PARENT)
	{
		for (auto it = PARENT.begin();it!=PARENT.end();++it)
			cout<<" "<<it->first<< ":"<<it->second;
		cout<<endl;
	}
};
int main()
{
	Disjoint_set ds;
	ds.Find('c');
	ds.Union('c','a');
	ds.Union('a','b');
	ds.printParent();
	return 0;
}
