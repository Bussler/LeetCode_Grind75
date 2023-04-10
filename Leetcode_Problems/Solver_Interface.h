#pragma once

namespace LeetcodeSolving{

// M: Interace for Problem class: Arbitrary input and output and have solve method
template<typename Output, typename... Input>
class SolverInterface {
public:
  virtual ~SolverInterface() = default;
  virtual Output solve(const Input&... input) = 0;
};


// M: Example usecase
class SquareSolver : public SolverInterface<int, int> {
public:
  int solve(const int& input) override {
    int result = input * input;
    return result;
  }
};

}
