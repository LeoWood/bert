#!/bin/bash
#SBATCH -p normal
#SBATCH -N 1
#SBATCH --exclusive
#SBATCH --mem=100G
#SBATCH -J 512_rest
#SBATCH -o create_pre_data_cscd_all_wwm_512_rest.out


python create_ernie_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_all_wwm/pre_training_TU_cscd_512_wwm_cmesh.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw/TU.txt \
 --max_seq_length 512
python create_ernie_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_all_wwm/pre_training_TV_cscd_512_wwm_cmesh.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw/TV.txt \
 --max_seq_length 512