#include <iostream>
#include "alpha.h"
#include "beta.h"

void f_beta(int n)
{
    f_alpha(n);
    std::cout << "f_beta:" << n << std::endl;
    return;
}
