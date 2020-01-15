#!/usr/bin/env bash
python run_classifier.py\
 --data_dir data/data_refind/data_mask_label/seq_length_nums\
 --bert_config_file models/uncased_L-12_H-768_A-12/bert_config.json\
 --task_name cla\
 --vocab_file models/uncased_L-12_H-768_A-12/vocab.txt\
 --output_dir outputs/Move_mask_label_refind_2e-5\
 --init_checkpoint models/uncased_L-12_H-768_A-12/bert_model.ckpt\
 --max_seq_length 313\
 --do_train True\
 --do_predict True\
 --train_batch_size 10\
 --learning_rate 2e-5\
 --num_train_epochs 3.0\
 --gpu 0\
 --cla_nums 5


