#!/bin/bash
#SBATCH -p normal
#SBATCH -N 1
#SBATCH -J pre_64
#SBATCH -o Pre1_cscd_R_128_64_from_scrach.out

/public/software/deeplearning/anaconda3/bin/python3 run_pretraining.py\
 --input_file /public/home/zzx6320/lh/Projects/bert/data/cscibert_pre_training/pre_training_R_cscd_128.tfrecord\
 --bert_config_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/bert_config.json\
 --output_dir /public/home/zzx6320/lh/Projects/bert/outputs/Pre1_cscd_R_128_64_from_scrach\
 --max_seq_length 128\
 --do_train True\
 --train_batch_size 64\
 --learning_rate 2e-5\
 --num_train_steps 1000000\
 --save_checkpoints_steps 100000\
 --gpu 0
