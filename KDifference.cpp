/* Enter your code here. Read input from STDIN. Print output to STDOUT */
#include <set>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
long long N, K;
/*
PASSED

*/
int main(int argc, char** argv) {
    cin >> N >> K;
    vector<long long> V(N, 0);
    for (int t = 0; t < N; t++) {
        cin >> V[t];
    }
    sort(V.begin(), V.end());
    int ret = 0;
    for (int i = 0; i < V.size()-1; i++) {
        for (int j = i + 1; j < V.size(); j++) {
            if (V[j] - V[i] == K) {
                ret++;
                break;
            } else if (V[j] - V[i] > K) {
                break;
            }
        }
    }
    cout << ret;
    return 0;
}
