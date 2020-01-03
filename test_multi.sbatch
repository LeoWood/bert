#!/bin/bash
#SBATCH -p debug
#SBATCH -N 4
#SBATCH -J test_multi_data_16000

mpirun -np 4 multi_test.sh
