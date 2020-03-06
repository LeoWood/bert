#!/bin/bash
#SBATCH -p normal
#SBATCH -N 1
#SBATCH --exclusive
#SBATCH -J data_test
#SBATCH -o data_test_12.out

python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file data_test_128.tfrecord \
 --input_file pre_data_test.txt \
 --max_seq_length 128

python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file data_test_512.tfrecord \
 --input_file pre_data_test.txt \
 --max_seq_length 512

python create_ernie_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file data_test_128_wwm.tfrecord \
 --input_file pre_data_test.txt \
 --max_seq_length 128

python create_ernie_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file data_test_512_wwm.tfrecord \
 --input_file pre_data_test.txt \
 --max_seq_length 512