#!/bin/bash
#SBATCH -p normal
#SBATCH -N 1
#SBATCH --mem=120G
#SBATCH -J create_pre_data_cscd_all
#SBATCH -o create_pre_data_cscd_all_r.out


python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_all/pre_training_R_cscd_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw/R.txt \
 --max_seq_length 128
