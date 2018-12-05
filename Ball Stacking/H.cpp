#include <cstring>
#include <iostream>

using namespace std;

#define maxn 1000

int num, matriz[maxn][maxn];
int suma[maxn][maxn + 1];
long long memo[maxn][maxn];
bool oki[maxn][maxn];

long long resolver(int fila, int col){
    if(fila == num){
      return 0;
    }
    long long &sol = memo[fila][col];

    if(!oki[fila][col]){
        oki[fila][col] = true;
        sol = 0;

        if(col > 0) {
          sol = max(sol, resolver(fila, col - 1));
        }
        sol = max(sol,resolver(fila + 1,min(num - 2 - fila, col)) + suma[fila][col + 1]);
    }

    return sol;
}

int main(){
    while(true){
        scanf("%d",&num);
        if (num == 0){
            break;
        }


        for(int i = 0;i < num; i++){
          for(int j = 0;j <= i; j++){
            scanf("%d", &matriz[j][i - j]);
          }

        }


        for(int i = 0; i < num; i++){
          for(int j = 0; j < num - i; j++){
            suma[i][j + 1] = matriz[i][j] + suma[i][j];
          }

        }


        memset(oki, false, sizeof oki);
        printf("%lld\n", resolver(0, num - 1));
    }

    return 0;
}
