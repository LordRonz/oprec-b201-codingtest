#!/usr/bin/env bash

for (( i=1; i <= 3; ++i ))
do
    cd test-problem-$i
    python generate_testcase_sharif.py
    cd ../
done

cd problem-sanity-check
python generate_testcase_sharif.py
cd ../

for (( i=0; i <= 5; ++i ))
do
    cd problem-$i
    python generate_testcase_sharif.py
    cd ../
done
