#!/usr/bin/env bash
python run_classifier.py\
 --data_dir=data/cla_cscd_v\
 --bert_config_file=models/chinese_L-12_H-768_A-12/bert_config.json\
 --task_name=cla\
 --vocab_file=models/chinese_L-12_H-768_A-12/vocab.txt\
 --output_dir=outputs/Cla_cscd_v_base\
 --init_checkpoint=models/chinese_L-12_H-768_A-12/bert_model.ckpt\
 --max_seq_length=400\
 --do_train=True\
 --do_evalv=True\
 --do_predict=True\
 --train_batch_size=8\
 --learning_rate=2e-5\
 --num_train_epochs=3.0\
 --gpu=1\
 --cla_nums=49

python run_classifier.py\
 --data_dir=data/cla_cscd_x\
 --bert_config_file=models/chinese_L-12_H-768_A-12/bert_config.json\
 --task_name=cla\
 --vocab_file=models/chinese_L-12_H-768_A-12/vocab.txt\
 --output_dir=outputs/Cla_cscd_x_base\
 --init_checkpoint=models/chinese_L-12_H-768_A-12/bert_model.ckpt\
 --max_seq_length=400\
 --do_train=True\
 --do_evalv=True\
 --do_predict=True\
 --train_batch_size=8\
 --learning_rate=2e-5\
 --num_train_epochs=3.0\
 --gpu=1\
 --cla_nums=78

python run_classifier.py\
 --data_dir=data/cla_cscd_tq\
 --bert_config_file=models/chinese_L-12_H-768_A-12/bert_config.json\
 --task_name=cla\
 --vocab_file=models/chinese_L-12_H-768_A-12/vocab.txt\
 --output_dir=outputs/Cla_cscd_tq_base\
 --init_checkpoint=models/chinese_L-12_H-768_A-12/bert_model.ckpt\
 --max_seq_length=400\
 --do_train=True\
 --do_evalv=True\
 --do_predict=True\
 --train_batch_size=8\
 --learning_rate=2e-5\
 --num_train_epochs=3.0\
 --gpu=1\
 --cla_nums=88

python run_classifier.py\
 --data_dir=data/cla_cscd_tm\
 --bert_config_file=models/chinese_L-12_H-768_A-12/bert_config.json\
 --task_name=cla\
 --vocab_file=models/chinese_L-12_H-768_A-12/vocab.txt\
 --output_dir=outputs/Cla_cscd_tm_base\
 --init_checkpoint=models/chinese_L-12_H-768_A-12/bert_model.ckpt\
 --max_seq_length=400\
 --do_train=True\
 --do_evalv=True\
 --do_predict=True\
 --train_batch_size=8\
 --learning_rate=2e-5\
 --num_train_epochs=3.0\
 --gpu=1\
 --cla_nums=69

 python run_classifier.py\
 --data_dir=data/cla_cscd_tn\
 --bert_config_file=models/chinese_L-12_H-768_A-12/bert_config.json\
 --task_name=cla\
 --vocab_file=models/chinese_L-12_H-768_A-12/vocab.txt\
 --output_dir=outputs/Cla_cscd_tn_base\
 --init_checkpoint=models/chinese_L-12_H-768_A-12/bert_model.ckpt\
 --max_seq_length=400\
 --do_train=True\
 --do_evalv=True\
 --do_predict=True\
 --train_batch_size=8\
 --learning_rate=2e-5\
 --num_train_epochs=3.0\
 --gpu=1\
 --cla_nums=101