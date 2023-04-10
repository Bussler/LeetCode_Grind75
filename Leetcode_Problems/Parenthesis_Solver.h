#pragma once
#include "Solver_Interface.h"
#include <iostream>
#include <string>
#include <stack>

using namespace LeetcodeSolving;
using namespace std;


// M: Given a list of numbers, give the indices of the numbers summing to a target number
class ParenthesisSolver : public SolverInterface<bool, string> {
public:
  bool solve(const string& s) override {
    
    std::stack<char> myStack;

        for (char c : s){

            switch (c) {
                case ')':
                    if (myStack.empty() || myStack.top() != '('){
                        return false;
                    }
                    myStack.pop();
                    break;
                case '}':
                    if (myStack.empty() || myStack.top() != '{'){
                        return false;
                    }
                    myStack.pop();
                    break;
                case ']':
                    if (myStack.empty() || myStack.top() != '['){
                        return false;
                    }
                    myStack.pop();
                    break;
                default:
                    myStack.push(c);
                    break;
            }

        }

        return myStack.empty();
    
  }
};