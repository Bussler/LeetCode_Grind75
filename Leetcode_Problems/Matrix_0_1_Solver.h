#pragma once
#include "Solver_Interface.h"
#include <iostream>
#include <vector>
#include <queue>

using namespace LeetcodeSolving;
using namespace std;

vector<int> DIR_PLACEHOLDER = {0, 1, 0, -1, 0};


class Matrix_0_1_Solver : public SolverInterface<void> {
public:

   void solve() override {


  }

  vector<vector<int>> solve(vector<vector<int>>& mat) {
    
    // Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
    // M: simple idea: do bfs from 0 points -> then starting from 0s, update parents: Simply add 1 to distance
    // M: Manage unseen elements in queue

    queue<pair<int, int>> q;

    // M: fill queue by finding all 0 to start with
    for(int i = 0; i<mat.size(); i++){

        for(int j = 0; j< mat[0].size(); j++){
            if(mat[i][j] == 0){
                q.emplace(i, j);
            }
            else{
                // M: invalidate not-0 elements to show the bfs that this element was not yet visited
                mat[i][j] == -1;
            }
        }
    }

    // M: do the bfs
    while (!q.empty())
    {
        auto pair = q.front();
        int row = pair.first;
        int col = pair.second;
        q.pop();

        // M: search all four directions and put element into queue, if not previously visited
        for (int i = 0; i < 4; i++)
        {
            int n_row = DIR_PLACEHOLDER[i];
            int n_col = DIR_PLACEHOLDER[i+1];

            // M: check that we dont go out of bounds here
            if(n_row < 0 || n_col < 0 || n_row > mat.size() || n_col > mat[0].size()){
                continue;
            }

            if(mat[n_row][n_col] == -1){
                mat[n_row][n_col] = mat[row][col] + 1;
                q.emplace(n_row, n_col);
            }
        }
        

    }

    return mat;
  }


    void test_solve(){
        vector<vector<int>> mat = {{0,0,0},{0,1,0},{1,1,1}};

        auto distance_zero_mat = solve(mat);

        std::cout << "Output: "<<std::endl;
        for(auto i : distance_zero_mat){
            for (auto j: i){
                std::cout << j << " ";
            }
        }
        std::cout << std::endl;

    }

};
