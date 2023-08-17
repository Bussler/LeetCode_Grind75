#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>
#include <tuple>

// For smart pointer
#include <memory>

using namespace std;

template <typename T>
bool my_greater(const T &val1, const T &val2)
{
    return val1 > val2;
}


class my_test_class
{
public:
    my_test_class(int a){
        this->v2 = a;
    }

    my_test_class(int* a): p1(a) {}

    ~my_test_class(){

    }

private:
    int* p1;
    int v2;
};


int main(int argc, char const *argv[])
{
    bool dab = my_greater<int>(2, 1);
    cout << dab << std::endl;
    cout << my_greater(1,2) << endl;

    double thresh = 0.0001;
    auto lambda_funct = [&thresh](double d ) -> double {
        if (d < thresh){
            thresh = 30;
            return 10;
        }
        else
            return 20;
    }; // [ & ] in the capture clause: access by reference; without: access by value; (): argument list; -> return type

    cout << lambda_funct(0.00001) << " " << lambda_funct(0.1) << " " << thresh << endl;

    unique_ptr<int> p(new int(40)); //new keyword: allocate storage on stack (e.g. pointers); otherwise: heap
    cout << *p << endl;

    my_test_class t(new int(1));

    my_test_class t2(2);

    my_test_class* p2 = new my_test_class(1);
    delete p2;

    return 0;
}
