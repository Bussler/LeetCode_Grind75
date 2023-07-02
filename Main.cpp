#include <iostream>
#include <vector>
#include <string>
#include <tuple>
#include "Leetcode_Problems/ConcatString_Solver.h"
#include "Leetcode_Problems/SumTwo_Solver.h"
#include "Leetcode_Problems/Parenthesis_Solver.h"
#include "Leetcode_Problems/SortedListMerger_Solver.h"
#include "Leetcode_Problems/Matrix_0_1_Solver.h"
#include "Leetcode_Problems/K_Closest_Points_Solver.h"
#include "Leetcode_Problems/EvaluateReversePolishNotion_Solver.h"
#include "Leetcode_Problems/Coin_Change_Solver.h"

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

    /*ParenthesisSolver p_s;
    string example = "({})";
    bool res = p_s.solve(example);
    std::cout << "Parenthesis: "<< res << std::endl;


    LinkedListSolver l_s;
    ListNode* l1 = new ListNode(1);
    ListNode* l2 = new ListNode(1);
    ListNode* l3 = new ListNode(2);
    ListNode* l4 = new ListNode(2);

    l1->next = l4;
    l2->next = l3;

    ListNode* merged_list = l_s.solve(l1, l2);*/

    //Matrix_0_1_Solver mat_solver;
    //mat_solver.test_solve();

    //K_Closest_Solver c_solver;
    //c_solver.test_solve();

    //EvaluatePolischNotion_Solver r_solver;
    //r_solver.test_solve();

    Coin_Change_Solver c_solver;
    c_solver.test_solve();

    return 0;
}