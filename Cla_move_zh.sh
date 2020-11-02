#!/usr/bin/env bash
python run_classifier.py\
 --data_dir=data/move_zh_all_no_test\
 --bert_config_file=models/chinese_L-12_H-768_A-12/bert_config.json\
 --task_name=cla\
 --vocab_file=models/chinese_L-12_H-768_A-12/vocab.txt\
 --output_dir=outputs/Cla_move_zh_all_no_test\
 --init_checkpoint=models/chinese_L-12_H-768_A-12/bert_model.ckpt\
 --max_seq_length=128\
 --do_train=True\
 --train_batch_size=32\
 --learning_rate=2e-5\
 --num_train_epochs=3.0\
 --gpu=1\
 --cla_nums=4