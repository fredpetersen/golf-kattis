#! usr/bin/env python3
import sys
import re

line = sys.stdin.readline()
assert re.match(r"\d+ \d+", line)
n, m = map(int, line.split())

assert 2 <= n <= 100
assert 1 <= m <= 500

for i in range(n):
    personline = sys.stdin.readline()
    regex = r"((^| )(0|[-+][1-9][0-9]?))+\n" # each line contains m digits with spaces inbetween, no whitespace after last digit before \n
    assert re.match(regex, personline), personline
    k = list(map(int, personline.split()))
    for j in k:
        assert -100 < j < 100


assert sys.stdin.readline() == "" # no junk at the end

sys.exit(42) # exit kattis-fully