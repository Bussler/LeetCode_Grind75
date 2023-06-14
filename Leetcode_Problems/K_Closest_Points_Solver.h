#pragma once
#include "Solver_Interface.h"
#include <iostream>
#include <vector>
#include <queue>
#include <cmath>

using namespace LeetcodeSolving;
using namespace std;


float euclidian_distance(vector<int>& p1, vector<int> p2){
    return sqrt(pow(p1[0]-p2[0], 2) + pow(p1[1]-p2[1], 2));
}

class Compare {
public:
    bool operator()(pair<int, float> p1, pair<int, float> p2) {
        return p1.second >= p2.second;
    }
};


class K_Closest_Solver : public SolverInterface<void> {
public:

    void solve() override {
    }

    vector<vector<int>> solve(vector<vector<int>>& points, int k) {
    
        // Find k nearest points from origin
        // M: simple idea: calculate euclidian distance for each point and arrange them in priority queue

        std::priority_queue<pair<int, float>, std::vector<pair<int, float>>, Compare> ordered_list;
        int i =0;

        for (auto elem : points){
            float distance = euclidian_distance(elem, vector<int>{0,0});
            ordered_list.push({i++, distance});
        }

        vector<vector<int>> closest_points;
        for (int i=0; i<k; i++){
            int index = ordered_list.top().first;
            closest_points.push_back(points[index]);
            ordered_list.pop();
        }

        return closest_points;

    }


    void test_solve(){
        vector<vector<int>> points = {{3,3},{5,-1},{-2,4}};
        int k = 2;

        auto closest_points = solve(points, k);

        std::cout << "Output: "<<std::endl;
        for(auto i : closest_points){
            for (auto j: i){
                std::cout << j << " ";
            }
            std::cout << std::endl;
        }

    }

};
