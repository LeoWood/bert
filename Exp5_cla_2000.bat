python run_classifier.py^
 --data_dir data/cla_cscd_2000^
 --bert_config_file models/chinese_L-12_H-768_A-12/bert_config.json^
 --task_name cla^
 --vocab_file models/chinese_L-12_H-768_A-12/vocab.txt^
 --output_dir outputs/Exp5_cla_cscd_2000^
 --init_checkpoint models/chinese_L-12_H-768_A-12/bert_model.ckpt^
 --max_seq_length 400^
 --do_train True^
 --do_predict True^
 --train_batch_size 8^
 --learning_rate 2e-5^
 --num_train_epochs 2.0^
 --gpu 1^
 --cla_nums 81

