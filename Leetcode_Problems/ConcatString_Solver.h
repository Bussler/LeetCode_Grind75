#pragma once
#include "Solver_Interface.h"
#include <iostream>
#include <string>
#include <vector>

using namespace LeetcodeSolving;
using namespace std;


class StringConcatSolver : public SolverInterface<string, vector<string>> {
public:
  std::string solve(const vector<string>& input) override {
    std::string result = "";
    for(const string& word : input)
    {
        result+= word + " ";
    }
    std::cout << "Concatenating strings yields: "<< std::endl << result << std::endl;
    return result;
  }
};
