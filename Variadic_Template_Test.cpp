#include <string>
#include <iostream>


class Solver {
public:
    //virtual void solve() = 0;
    virtual ~Solver() = default;
};

template <typename R, typename... Args>
class SolverWithArgs{
public:
    virtual R solve(Args... args) = 0;
    virtual ~SolverWithArgs() = default;
};

class MySolver : public SolverWithArgs<int, int, float> {
public:
    //void solve() override {
    //    solve(0, 0.0f);
    //}

    int solve(int x, float y) override {
        std::cout << x << std::endl;
        return x+y;
    }
};

int main() {
    MySolver solver;
    float c = solver.solve(42, 3.14f);
    return 0;
}

