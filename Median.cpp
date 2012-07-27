/* Sample program illustrating input and output */

#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <sstream>
using namespace std;
/*
N is too large for naive O(N^2) approach.

PASSED
strategy:
use two heap: minH(n/2~n), maxH(0~n/2)
invariant: abs(minH.size() - maxH.size()) <= 1
median: 
minH.size() + maxH.size() is even: (minH.top() + maxH.top()) / 2
odd => if minH.size() > maxH.size(): minH.top()
else: maxH.top()
*/


int main(){
	int N;
	cin >> N;
	multiset<int> lowH, highH;
	multiset<int>::iterator it;

	for(int i = 0; i < N; i++){
		long long int median = 0;
		string s;
		int x;
		cin >> s >> x;
		bool found = true;
		if (s == "a") {
			if (lowH.size() == 0) lowH.insert(x);
			else {
				it = lowH.end(); it--;
				if (x < *it) lowH.insert(x);
				else highH.insert(x);
			}
		} else if (s == "r") {
			if (lowH.find(x) != lowH.end()) {
				lowH.erase(lowH.find(x));
			} else if (highH.find(x) != highH.end()) {
				highH.erase(highH.find(x));
			} else {
				found = false;
			}
		}
		int diff = lowH.size() - highH.size();
		diff = diff < 0 ? -diff : diff;
		if (diff > 1) {
			if (lowH.size() > highH.size() + 1) {
				it = lowH.end(); it--;
				highH.insert(*it);
				lowH.erase(it);
			}
			if (highH.size() > lowH.size() + 1) {
				it = highH.begin();
				lowH.insert(*it);
				highH.erase(it);
			}
		}
		if (!found || (lowH.size() == 0 && highH.size() == 0)) {
			cout << "Wrong!" << endl;
		} else if (lowH.size() == highH.size()) {
			it = lowH.end(); it--;
			median += *it;
			it = highH.begin();
			median += *it;
			if (median % 2 == 0) {
				printf("%.0lf\n", median / 2.0);
			} else {
				printf("%.1lf\n", median / 2.0);
			}
		} else if (lowH.size() > highH.size()) {
			it = lowH.end(); it--;
			median = *it;
			cout << median << endl;
		} else if (highH.size() > lowH.size()) {
			it = highH.begin();
			median = *it;
			cout << median << endl;
		}
	}
	
	return 0;	
}
