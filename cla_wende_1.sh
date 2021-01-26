#!/usr/bin/env bash
python run_classifier.py\
 --data_dir=data/cla_wende/cla_1\
 --bert_config_file=models/chinese_L-12_H-768_A-12/bert_config.json\
 --task_name=cla\
 --vocab_file=models/chinese_L-12_H-768_A-12/vocab.txt\
 --output_dir=outputs/Cla_wende_1_base\
 --init_checkpoint=models/chinese_L-12_H-768_A-12/bert_model.ckpt\
 --max_seq_length=128\
 --do_train=True\
 --do_eval True\
 --do_predict True\
 --train_batch_size=32\
 --learning_rate=2e-5\
 --num_train_epochs=5.0\
 --gpu=0\
 --cla_nums=2