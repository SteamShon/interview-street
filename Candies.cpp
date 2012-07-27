#include <iostream>
#include <vector>
#include <map>
/*
PASSED
use greedy approach
*/
using namespace std;
int N;
int dir[] = {-1, 1};

int main(int argc, char** argv) {
	cin >> N;
	vector<int> R(N, 0);
	vector<int> V(N, 1);
	for (int t = 0; t < N; t++) {
		cin >> R[t];
	}
	int iter = 0;
	while (true) {
		cout << "iteration: " << iter++ << endl;
		bool finished = true;
		for (int i = 0; i < R.size(); i++) {
			for (int k = 0; k < 2; k++) {
				// now we are check next element 
				int next = i + dir[k];
				if (next >= 0 && next < N) {
					if (R[next] > R[i] && V[next] <= V[i]) {
						// relax current element`s value vector V
						cout << "update: " << V[i] << " => " << V[next] << endl;
						V[next] = V[i] + 1;
						finished = false;
					}
				}
			}
		}
		for (int i = 0; i < V.size(); i++) {
			cout << V[i] << " ";
		}
		cout << endl;
		if (finished) break;
	}
	int sum = 0;
	for (int i = 0; i < V.size(); i++) {
		sum += V[i];
		cout << V[i] << " ";
	}
	cout << endl;
	cout << sum << endl;
	return 0;
}
