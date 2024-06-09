#include <iostream>
// using namespace std;

int main() {
    int num1, num2, sum;

    // Input the two integers
    std::cout << "Enter first integer: ";
    std::cin >> num1;

    std::cout << "Enter second integer: ";
    std::cin >> num2;

    // by line 2: namespace
    // std::cout << "Enter first integer: ";
    // becomes: 
    // cout << "Enter first integer: ";


    // Calculate the sum
    sum = num1 + num2;

    // Display the result
    std::cout << "Sum of the two integers is: " << sum << std::endl;

    return 0;
}
