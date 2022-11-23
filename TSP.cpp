#include <iostream>
#include <vector>
#include <algorithm>
#include <time.h>
#include <chrono>
#include <math.h>

using namespace std;

bool nextPermutation(vector<int>& nums) {
    int sz = nums.size();
    if (sz <= 1) return true;
    int i = sz - 2;
    // find the decreasing element
    while ((i >= 0) && (nums[i] >= nums[i + 1])) --i;
    if (i >= 0) { // if there is..
        int j = sz - 1;
        // find next larger number
        while ((j >= i) && (nums[j] <= nums[i])) {
            --j;
        }
        swap(nums[i], nums[j]);
    }
    std::reverse(begin(nums) + i + 1, end(nums));

    for(i  = 0; i < nums.size()-1; i++)
        if(nums[i] > nums[i+1]) return true;

    return false;
}

// unsigned seed = std::chrono::system_clock::now().time_since_epoch().count(); 

double calcDist(const vector<int>& route, const vector<vector<double>>& mtrDist) {
    double total = mtrDist[0][route[0]] + mtrDist[route[route.size() - 1]][0];

    /*
    * temos que somar a distancia da cidade do caixeiro
    * até a primeira cidade da rota, e devemos somar a distância da
    * ultima cidade da rota até a cidade do caixeiros
    */

    for (int i = 0; i < route.size() - 1; i++)
        total += mtrDist[route[i]][route[i + 1]];

    return total;
}

int main(int argc, char** argv) {
    int n, aux;
    double minDist;
    bool isFirstMin = false;
    srand(time(NULL));

    //le a matriz n*n de distancias
    if (argc > 1) n = atoi(argv[1]); //se tivermos parametros entra no modo de teste de tempo e aloca a matriz automaticamente
    else cin >> n;

    vector<vector<double>> mtrDist(n);
    vector<pair<int, int>> coords(n);
    vector<int> pointsIDs, bestRoute;

    for (int i = 0;i < n;i++) {
        cin >> coords[i].first >> coords[i].second;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            //seta as posiçoes da matriz aleatoriamente
            int dx = coords[i].first - coords[j].first;
            int dy = coords[i].second - coords[j].second;
            mtrDist[i].push_back(sqrt((dx * dx) + (dy * dy)));
        }
    }

    for (int i = 0; i < n - 1; i++)
        pointsIDs.push_back(i + 1);
    std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();
    double tempo;

    do {
        double auxDist = calcDist(pointsIDs, mtrDist);
        //assume como melhor rota a primeira(so executa na primeira iteração :)
        if (!isFirstMin) {
            minDist = auxDist;
            bestRoute = pointsIDs;
            isFirstMin = true;
        }
        else if (auxDist < minDist) {
            minDist = auxDist;
            bestRoute = pointsIDs;
        }
        std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
        tempo = std::chrono::duration_cast<std::chrono::milliseconds> (end - begin).count();
    } while (nextPermutation(pointsIDs) and tempo <= 3.6e6);

    cout << minDist << '\n';
    cout << tempo << "ms \n";
    //imprime a melhor rota
    cout << "0 -> ";
    for (int i = 0; i < n - 1; i++)
        cout << bestRoute[i] << " -> ";

    cout << "0\n";

    return 0;
}