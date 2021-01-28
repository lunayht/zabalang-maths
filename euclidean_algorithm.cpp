#include <iostream>

long long lcm_naive(int a, int b) {
        for (long l = 1; l <= (long long) a * b; ++l)
                if (l % a == 0 && l % b == 0)
                return l;

        return (long long) a * b;
}

unsigned long long gcd_fast(int a, int b) {
        if (b == 0 ) {
                return a;
        }
        if (b > a) {
                a, b = b, a;
        }
        return gcd_fast(b, a % b);
}

unsigned long long lcm_fast(int a, int b) {
        unsigned long long gcd = gcd_fast(a, b);
        return (unsigned long long) gcd * (a / gcd) * (b / gcd);
}

int main() {
/*
        while (true) {
                int a = rand() % 30 + 1;
                int b = rand() % 30 + 1;
                std::cout << a << " " << b << "\n";
                long long res1 = lcm_naive(a, b);
                unsigned long long res2 = lcm_fast(a, b);
                if (res1 != res2) {
                        std::cout << res1 << " " << res2;
                        break;
                }
                std::cout << "OK\n";
        }
*/
        int a, b;
        std::cin >> a >> b;
        std::cout << lcm_fast(a, b) << std::endl;
        return 0;
}