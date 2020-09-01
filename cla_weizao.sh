python run_classifier.py\
 --data_dir data/xiandao/weizao\
 --bert_config_file models/uncased_L-12_H-768_A-12/bert_config.json\
 --task_name cla\
 --vocab_file models/uncased_L-12_H-768_A-12/vocab.txt\
 --output_dir outputs/Cla_xiandao_weizao\
 --init_checkpoint models/uncased_L-12_H-768_A-12/bert_model.ckpt\
 --max_seq_length 200\
 --do_train True\
 --do_eval True\
 --do_predict True\
 --train_batch_size 20\
 --learning_rate 2e-5\
 --num_train_epochs 5.0\
 --gpu 0\
 --cla_nums 9


