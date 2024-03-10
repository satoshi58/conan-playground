#include <iostream>
#include "alpha.h"
#include "delta.h"
#include "epsilon.h"

void f_epsilon(int n)
{
    f_alpha(n-2);
    f_delta(n+2);
    std::cout << "f_epsilon:" << n << std::endl;
    return;
}
