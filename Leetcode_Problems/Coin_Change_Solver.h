#pragma once
#include "Solver_Interface.h"
#include <iostream>
#include <vector>
#include <stack>
#include <string>
#include <unordered_map>
#include <limits>

using namespace LeetcodeSolving;
using namespace std;

// M: Given a target amount and a list of possible coins, return the amount of coins needed to reach that amount
class Coin_Change_Solver : public SolverInterface<int, vector<int>, int>
{
public:
    unordered_map<int, int> ht;

    int recursive_solving(const vector<int> &coins, const int &amt)
    {

        if (amt == 0)
        {
            return 0;
        }

        // M: Checking if a key exists
        if (ht.find(amt) != ht.end())
        {
            return ht[amt];
        }

        int coin_steps = std::numeric_limits<int>::max();

        for (auto &&elem : coins)
        {
            if (elem <= amt)
            {
                coin_steps = min(coin_steps, recursive_solving(coins, amt - elem) + 1);
            }
        }

        ht[amt] = coin_steps;
        return coin_steps;
    }

    int solve(const vector<int> &coins, const int &amt) override
    {
        // M: Idea: manage global hashtable that holds amounts that were encountered before!
        // -> So if we iterate over all possible combinations we can earlier cross out some!

        int steps = recursive_solving(coins, amt);

        if (steps == std::numeric_limits<int>::max())
        {
            return -1;
        }

        return steps;
    }

    void test_solve()
    {
        vector<int> coins = {1, 2, 5};
        int amount = 11;

        auto res = solve(coins, amount);

        std::cout << "Result: " << res << std::endl;
    }
};
