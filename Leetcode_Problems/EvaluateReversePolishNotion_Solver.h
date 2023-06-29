#pragma once
#include "Solver_Interface.h"
#include <iostream>
#include <vector>
#include <stack>
#include <string>

using namespace LeetcodeSolving;
using namespace std;

// M: Given a list of numbers, give the indices of the numbers summing to a target number
class EvaluatePolischNotion_Solver : public SolverInterface<int, vector<string>>
{
public:
    int solve(const vector<string> &tokens) override
    {
        /*
        M:
        The valid operators are '+', '-', '*', and '/'.
        operators follow their operands: 3 4 + = 3 + 4

        Idea: Use stack -> Put elements on stack, when encountering operator consume the two last elements from stack and put result back on stack.
        In the end return stack
        */

        stack<int> number_stash;

        auto return_top_two_elements = [&number_stash]() -> std::pair<int, int>
        {
            auto elem1 = number_stash.top();
            number_stash.pop();
            auto elem2 = number_stash.top();
            number_stash.pop();
            return std::make_pair(elem2, elem1);
        };

        for (const string &elem : tokens)
        {

            if (elem == "*")
            {
                std::pair<int, int> s_elem = return_top_two_elements();
                int cur_res = s_elem.first * s_elem.second;
                number_stash.push(cur_res);
            }
            else if (elem == "/")
            {
                std::pair<int, int> s_elem = return_top_two_elements();
                int cur_res = s_elem.first / s_elem.second;
                number_stash.push(cur_res);
            }
            else if (elem == "-")
            {
                std::pair<int, int> s_elem = return_top_two_elements();
                int cur_res = s_elem.first - s_elem.second;
                number_stash.push(cur_res);
            }
            else if (elem == "+")
            {
                std::pair<int, int> s_elem = return_top_two_elements();
                int cur_res = s_elem.first + s_elem.second;
                number_stash.push(cur_res);
            }
            else
            {
                number_stash.push(stoi(elem));
            }
        }

        return number_stash.top();
    }

    void test_solve()
    {
        // vector<string> tokens = {"2", "1", "+", "3", "*"};
        vector<string> tokens = {"4", "13", "5", "/", "+"};

        auto res = solve(tokens);

        std::cout << "Result: " << res << std::endl;
    }
};
