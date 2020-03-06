#!/bin/bash
#SBATCH -p normal
#SBATCH -N 1
#SBATCH --exclusive
#SBATCH -J data_128
#SBATCH -o data_128.out


python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_O_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/O.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_P_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/P.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_Q_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/Q.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_R_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/R.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_S_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/S.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_U_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/U.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_V_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/V.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_X_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/X.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TB_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TB.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TD_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TD.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TE_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TE.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TF_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TF.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TG_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TG.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TH_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TH.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TJ_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TJ.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TK_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TK.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TL_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TL.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TM_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TM.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TN_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TN.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TP_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TP.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TQ_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TQ.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TS_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TS.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TU_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TU.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TV_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TV.txt \
 --max_seq_length 128