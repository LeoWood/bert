#!/usr/bin/env bash
python run_classifier.py\
 --data_dir data/data_refind/data_msm/aaa_seq_length\
 --bert_config_file models/uncased_L-12_H-768_A-12/bert_config.json\
 --task_name cla\
 --vocab_file models/uncased_L-12_H-768_A-12/vocab.txt\
 --output_dir outputs/Move_mask_sens_refind\
 --init_checkpoint models/uncased_L-12_H-768_A-12/bert_model.ckpt\
 --max_seq_length 512\
 --do_train True\
 --train_batch_size 5\
 --learning_rate 3e-5\
 --num_train_epochs 3.0\
 --gpu 1\
 --cla_nums 5

python run_classifier.py\
 --data_dir data/data_refind/data_msm/aaa_seq_length/test_mask\
 --bert_config_file models/uncased_L-12_H-768_A-12/bert_config.json\
 --task_name cla\
 --vocab_file models/uncased_L-12_H-768_A-12/vocab.txt\
 --output_dir outputs/Move_mask_sens_refind\
 --init_checkpoint models/uncased_L-12_H-768_A-12/bert_model.ckpt\
 --max_seq_length 512\
 --do_predict True\
 --train_batch_size 5\
 --learning_rate 3e-5\
 --num_train_epochs 3.0\
 --gpu 1\
 --cla_nums 5\
 --test_results_pre mask_

python run_classifier.py\
 --data_dir data/data_refind/data_msm/aaa_seq_length/test_sen\
 --bert_config_file models/uncased_L-12_H-768_A-12/bert_config.json\
 --task_name cla\
 --vocab_file models/uncased_L-12_H-768_A-12/vocab.txt\
 --output_dir outputs/Move_mask_sens_refind\
 --init_checkpoint models/uncased_L-12_H-768_A-12/bert_model.ckpt\
 --max_seq_length 512\
 --do_predict True\
 --train_batch_size 5\
 --learning_rate 3e-5\
 --num_train_epochs 3.0\
 --gpu 1\
 --cla_nums 5\
 --test_results_pre sen_

python test_merge.py\
 --data_dir data/data_refind/data_msm/aaa_seq_length/test_sen\
 --output_dir outputs/Move_mask_sens_refind


