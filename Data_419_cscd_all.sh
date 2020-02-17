#!/usr/bin/env bash
#cscd医学领域数据, max_seq 128, wwm

python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_all/pre_training_O_cscd_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw/O.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_all/pre_training_P_cscd_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw/P.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_all/pre_training_Q_cscd_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw/Q.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_all/pre_training_R_cscd_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw/R.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_all/pre_training_S_cscd_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw/S.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_all/pre_training_U_cscd_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw/U.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_all/pre_training_V_cscd_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw/V.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_all/pre_training_X_cscd_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw/X.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_all/pre_training_TB_cscd_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw/TB.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_all/pre_training_TD_cscd_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw/TD.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_all/pre_training_TE_cscd_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw/TE.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_all/pre_training_TF_cscd_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw/TF.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_all/pre_training_TG_cscd_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw/TG.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_all/pre_training_TH_cscd_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw/TH.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_all/pre_training_TJ_cscd_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw/TJ.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_all/pre_training_TK_cscd_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw/TK.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_all/pre_training_TL_cscd_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw/TL.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_all/pre_training_TM_cscd_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw/TM.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_all/pre_training_TN_cscd_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw/TN.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_all/pre_training_TP_cscd_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw/TP.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_all/pre_training_TQ_cscd_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw/TQ.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_all/pre_training_TS_cscd_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw/TS.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_all/pre_training_TU_cscd_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw/TU.txt \
 --max_seq_length 128
python create_pretraining_data.py \
 --vocab_file /public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/vocab.txt \
 --output_file /work1/zzx6320/lh/Projects/bert/data/cscd_all/pre_training_TV_cscd_128.tfrecord \
 --input_file /work1/zzx6320/lh/Projects/Data/Pretraining_Raw/TV.txt \
 --max_seq_length 128

