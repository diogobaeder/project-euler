#!/bin/bash

number=$1

mkdir $number

cat 0/problem0.py | sed "s/0/"$number"/g" > $number/problem$number.py
cat 0/test_problem0.py | sed "s/0/"$number"/g" > $number/test_problem$number.py
chmod +x $number/problem$number.py