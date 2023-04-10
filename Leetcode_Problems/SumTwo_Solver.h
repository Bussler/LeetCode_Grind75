#pragma once
#include "Solver_Interface.h"
#include <iostream>
#include <tuple>
#include <vector>
#include <unordered_map>

using namespace LeetcodeSolving;
using namespace std;


// M: Given a list of numbers, give the indices of the numbers summing to a target number
class SumTwoSolver : public SolverInterface<vector<int>, vector<int>, int> {
public:
  vector<int> solve(const vector<int>& nums, const int& target) override {
    
    //vector<int> nums = std::get<0>(input);
    //int target = std::get<1>(input);

    unordered_map<int, int> visited_hashmap;

        for(int i = 0; i<nums.size(); i++){
            int cur_n = nums[i];
            int target_left = target - cur_n;

            if(visited_hashmap.count(target_left)){
                return vector<int>{visited_hashmap[target_left], i};
            }

            visited_hashmap[cur_n] = i;

        }
        return std::vector<int>{-1};
  }
};