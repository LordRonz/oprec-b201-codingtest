#!/usr/bin/env bash

test_problem () {
    for (( i=1; i <= $1; ++i ))
    do
        ./a.out < testcase/$i.in | diff testcase/$i.out -
        if (( $? != 0 ))
        then
            echo "Solution is wrong on test $i"
            cat testcase/$i.in | tail -5
            pwd
            exit 69
        fi
    done
}

cd problem-sanity-check
gcc solution.c
test_problem 10

cd ../problem-0
gcc solution.c
test_problem 20

cd ../problem-1
g++ solution.cpp
test_problem 30

cd ../problem-2
g++ solution.cpp
test_problem 30

cd ../problem-3
g++ solution.cpp
test_problem 30

cd ../problem-4
g++ solution.cpp
test_problem 30

cd ../test-problem-0
gcc solution.c
test_problem 1

cd ../test-problem-1
g++ solution.cpp
test_problem 8

cd ../test-problem-2
g++ solution.cpp
test_problem 20

cd ../test-problem-3
g++ solution.cpp
test_problem 20

echo "Solutions verified !"
