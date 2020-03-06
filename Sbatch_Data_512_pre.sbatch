#!/bin/bash
#SBATCH -p normal
#SBATCH -N 1
#SBATCH --exclusive
#SBATCH --mem=100G
#SBATCH -J data_512
#SBATCH -o data_512.out


python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_O_512.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/O.txt \
 --max_seq_length 512
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_P_512.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/P.txt \
 --max_seq_length 512
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_Q_512.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/Q.txt \
 --max_seq_length 512
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_R_512.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/R.txt \
 --max_seq_length 512
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_S_512.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/S.txt \
 --max_seq_length 512
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_U_512.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/U.txt \
 --max_seq_length 512
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_V_512.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/V.txt \
 --max_seq_length 512
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_X_512.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/X.txt \
 --max_seq_length 512
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TB_512.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TB.txt \
 --max_seq_length 512
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TD_512.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TD.txt \
 --max_seq_length 512
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TE_512.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TE.txt \
 --max_seq_length 512
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TF_512.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TF.txt \
 --max_seq_length 512
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TG_512.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TG.txt \
 --max_seq_length 512
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TH_512.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TH.txt \
 --max_seq_length 512
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TJ_512.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TJ.txt \
 --max_seq_length 512
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TK_512.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TK.txt \
 --max_seq_length 512
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TL_512.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TL.txt \
 --max_seq_length 512
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TM_512.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TM.txt \
 --max_seq_length 512
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TN_512.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TN.txt \
 --max_seq_length 512
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TP_512.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TP.txt \
 --max_seq_length 512
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TQ_512.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TQ.txt \
 --max_seq_length 512
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TS_512.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TS.txt \
 --max_seq_length 512
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TU_512.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TU.txt \
 --max_seq_length 512
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_pre/pre_training_TV_512.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw_New/TV.txt \
 --max_seq_length 512