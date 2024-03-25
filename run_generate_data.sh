#!/bin/bash

CUDA_VISIBLE_DEVICES=0 nohup python generate_data.py 1 > ./logs/log0.txt 2>&1 &
CUDA_VISIBLE_DEVICES=1 nohup python generate_data.py 2 > ./logs/log1.txt 2>&1 &
CUDA_VISIBLE_DEVICES=2 nohup python generate_data.py 3 > ./logs/log2.txt 2>&1 &
CUDA_VISIBLE_DEVICES=3 nohup python generate_data.py 4 > ./logs/log3.txt 2>&1 &
CUDA_VISIBLE_DEVICES=4 nohup python generate_data.py 5 > ./logs/log4.txt 2>&1 &
CUDA_VISIBLE_DEVICES=5 nohup python generate_data.py 6 > ./logs/log5.txt 2>&1 &
CUDA_VISIBLE_DEVICES=6 nohup python generate_data.py 7 > ./logs/log6.txt 2>&1 &
CUDA_VISIBLE_DEVICES=7 nohup python generate_data.py 8 > ./logs/log7.txt 2>&1 &
