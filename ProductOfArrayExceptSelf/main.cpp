#include <iostream>
#include <vector>

// C++11 lest unit testing framework
#include "lest.hpp"

using namespace std;


vector<int> getProductsOfAllIntsExceptAtIndex(const vector<int>& intVector)
{
    // make a vector with the products
    auto vSize = intVector.size();
    if (vSize<2){
        throw exception();
    }

    auto res = vector<int>(vSize, 1);
    long currTotalLeft = intVector[0];
    long currTotalRight = intVector[vSize-1];
    for (unsigned int i=1; i< vSize; ++i){
        res[i] *= currTotalLeft;
        currTotalLeft *= intVector[i];
        res[vSize-i-1] *= currTotalRight;
        currTotalRight *= intVector[vSize-i-1];
    }
    return res;
}


const lest::test tests[] = {
    {CASE("small vector") {
        const auto actual = getProductsOfAllIntsExceptAtIndex({1, 2, 3});
        const auto expected = vector<int> {6, 3, 2};
        EXPECT(actual == expected);
    }},

    {CASE("longer vector") {
        const auto actual = getProductsOfAllIntsExceptAtIndex({8, 2, 4, 3, 1, 5});
        const auto expected = vector<int> {120, 480, 240, 320, 960, 192};
        EXPECT(actual == expected);
    }},

    {CASE("vector has one zero") {
        const auto actual = getProductsOfAllIntsExceptAtIndex({6, 2, 0, 3});
        const auto expected = vector<int> {0, 0, 36, 0};
        EXPECT(actual == expected);
    }},

    {CASE("vector has two zeros") {
        const auto actual = getProductsOfAllIntsExceptAtIndex({4, 0, 9, 1, 0});
        const auto expected = vector<int> {0, 0, 0, 0, 0};
        EXPECT(actual == expected);
    }},

    {CASE("one negative number") {
        const auto actual = getProductsOfAllIntsExceptAtIndex({-3, 8, 4});
        const auto expected = vector<int> {32, -12, -24};
        EXPECT(actual == expected);
    }},

    {CASE("all negative numbers") {
        const auto actual = getProductsOfAllIntsExceptAtIndex({-7, -1, -4, -2});
        const auto expected = vector<int> {-8, -56, -14, -28};
        EXPECT(actual == expected);
    }},

    {CASE("error with empty vector") {
        EXPECT_THROWS(getProductsOfAllIntsExceptAtIndex({}));
    }},

    {CASE("error with one number") {
        EXPECT_THROWS(getProductsOfAllIntsExceptAtIndex({1}));
    }},
};

int main(int argc, char** argv)
{
    return lest::run(tests, argc, argv);
}
