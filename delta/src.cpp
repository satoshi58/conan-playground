#include <iostream>
#include "beta.h"
#include "gamma.h"
#include "delta.h"

void f_delta(int n)
{
    f_beta(n-1);
    f_gamma(n+1);
    std::cout << "f_delta:" << n << std::endl;
    return;
}
