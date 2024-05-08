#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
void generar_lenguaje(int n, int p) {
    vector<vector<int>> alfabeto(p + 1, std::vector<int>(n));
    for (int i = 0; i < n; ++i) {
        alfabeto[0][i] = i;
    }
    
    for (int i = 1; i <= p; ++i) {
        cout << "L^" << i << " = [";
        for (int j = 0; j < pow(n, i); ++j) {
            if (j != 0) {
                cout << ", ";
            }
            for (int k = i - 1; k >= 0; --k) {
                cout << alfabeto[k][j / static_cast<int>(pow(n, k)) % n];
            }
        }
        cout << "]" << std::endl;
    }
}

int main() {
    int n, p;
    cout << "Tamanio del alfabeto: ";
    cin >> n;
    cout << "Potencia del lenguaje: ";
    cin >> p;
    generar_lenguaje(n, p);
    return 0;
}
