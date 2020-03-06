#!/bin/bash
#SBATCH -p normal
#SBATCH -N 1
#SBATCH --exclusive
#SBATCH --mem=100G
#SBATCH -J wwm_512
#SBATCH -o data_wwm_512_rest_rest.out


python create_ernie_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre_wwm/pre_training_S_512_wwm.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/S.txt \
 --max_seq_length 512