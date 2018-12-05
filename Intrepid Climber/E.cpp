#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector< pair<int, int> > grilla[150000];

int amigues[150000], w = 0, solucion = 0;

void dfs(int u, int &amigos, int profundidad) {
	int v;
	int encontrados = 0;
	amigos = amigues[u];
	if (amigues[u]){
			solucion = max(solucion, profundidad);
	}

	for (int i = 0; i < grilla[u].size(); i++) {
		v = grilla[u][i].first;
		dfs(v, encontrados, profundidad + grilla[u][i].second);
		if (encontrados > 0) {
			w += grilla[u][i].second;
			amigos += encontrados;
		}
	}
}
int main() {
	int n, f, a, b, c;
	while (scanf("%d %d", &n, &f) == 2) {
		for (int i = 1; i <= n; i++){
			grilla[i].clear(), amigues[i] = 0;
		}


		for (int i = 1; i < n; i++) {
			scanf("%d %d %d", &a, &b, &c);
			grilla[a].push_back(make_pair(b, c));
		}
		for (int i = 0; i < f; i++) {
			scanf("%d", &a);
			amigues[a] = 1;
		}
		w = 0, solucion = 0;
		dfs(1, a, 0);
		printf("%d\n", w - solucion);
	}
	return 0;
}
