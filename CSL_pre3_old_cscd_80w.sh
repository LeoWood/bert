#!/usr/bin/env bash
python run_classifier.py\
 --data_dir=data/data_CSL\
 --bert_config_file=models/chinese_L-12_H-768_A-12/bert_config.json\
 --task_name=pair\
 --vocab_file=models/chinese_L-12_H-768_A-12/vocab.txt\
 --output_dir=outputs/CSL_pre3_old\
 --init_checkpoint=/home/leo/lh/Projects/bert/models/pre3_old\
 --max_seq_length=512\
 --do_train=True\
 --do_predict=True\
 --train_batch_size=5\
 --learning_rate=2e-5\
 --num_train_epochs=3.0\
 --gpu=1\
 --cla_nums=2

python run_classifier.py\
 --data_dir=data/data_CSL\
 --bert_config_file=models/chinese_L-12_H-768_A-12/bert_config.json\
 --task_name=pair\
 --vocab_file=models/chinese_L-12_H-768_A-12/vocab.txt\
 --output_dir=outputs/CSL_pre6_old\
 --init_checkpoint=/home/leo/lh/Projects/bert/models/pre6_old\
 --max_seq_length=512\
 --do_train=True\
 --do_predict=True\
 --train_batch_size=5\
 --learning_rate=2e-5\
 --num_train_epochs=3.0\
 --gpu=1\
 --cla_nums=2

python run_classifier.py\
 --data_dir=data/data_CSL\
 --bert_config_file=models/chinese_L-12_H-768_A-12/bert_config.json\
 --task_name=pair\
 --vocab_file=models/chinese_L-12_H-768_A-12/vocab.txt\
 --output_dir=outputs/CSL_cscd_from_bert_80w\
 --init_checkpoint=/home/leo/lh/Projects/bert/outputs/Pre2_cscd_R_128_from_bert/model.ckpt-2000000\
 --max_seq_length=512\
 --do_train=True\
 --do_predict=True\
 --train_batch_size=5\
 --learning_rate=2e-5\
 --num_train_epochs=3.0\
 --gpu=1\
 --cla_nums=2

