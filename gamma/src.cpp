#include <iostream>
#include "alpha.h"
#include "gamma.h"

void f_gamma(int n)
{
    f_alpha(n);
    std::cout << "f_gamma:" << n << std::endl;
    return;
}
