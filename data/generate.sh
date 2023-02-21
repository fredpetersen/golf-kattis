#!/bin/bash
USE_SCORING=0
. ../../_testdata_tools/gen.sh  

use_solution aguh.py              # Use ../submissions/accepted/aguh.py to generate answer files

compile generate_random.py
compile generate_pos.py

# Generate answers to sample cases
sample 1
sample 2


tc  random1 generate_random
tc  random2 generate_random
tc  random3 generate_random
tc  pos1 generate_pos
tc  pos2 generate_pos