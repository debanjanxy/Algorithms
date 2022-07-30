#include <bits/stdc++.h>
using namespace std;

int main(){
    set<int> s;

    s.insert(2);
    s.insert(5);
    s.insert(4);
    s.insert(2);
    s.insert(3);
    auto it = s.lower_bound(2);
    cout << "Lower bound for 2 " << " = " << (*it);
}