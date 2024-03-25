# coding=utf-8
# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

import json
import os
import random

all_text = []

for i_start in range(64):
    # if i_start % 10 == 0:
    #     print(i_start)
    file_path = "gen_data/gen.chunk."+str(i_start).zfill(2)+".jsonl"
    if os.path.exists(file_path):
        print(f"merge file: {file_path}")
        for line in open(file_path, 'r'):
            all_text.append(json.loads(line))

output_path = "gen_data/all_gen.jsonl"
with open(output_path, "a") as f:
    for i in range(len(all_text)):
        f.write(json.dumps(all_text[i]))
        f.write('\n')
    print(f"{len(all_text)} samples are merged at {output_path}")
