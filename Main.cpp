#include <iostream>
#include <vector>
#include <string>
#include <tuple>
#include "Leetcode_Problems/ConcatString_Solver.h"
#include "Leetcode_Problems/SumTwo_Solver.h"
#include "Leetcode_Problems/Parenthesis_Solver.h"

using namespace std;

int main()
{
    vector<string> msg {"Hello", "C++", "World", "from", "VS Code", "and the C++ extension!", "Maarten Test"};

    StringConcatSolver string_solver;
    string_solver.solve(msg);


    /*vector<int> i_list = {-1,-2,-3,-4,-5};
    int target = -8;
    SumTwoSolver s2_solver;
    auto res = s2_solver.solve(i_list, target);
    for(auto element : res){
        cout << element << std::endl;
    }*/

    ParenthesisSolver p_s;
    string example = "({})";
    bool res = p_s.solve(example);
    std::cout << "Parenthesis: "<< res << std::endl;

    return 0;
}