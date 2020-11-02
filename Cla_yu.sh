python run_classifier.py\
 --data_dir work/yu_cla/data_20_percent_test\
 --bert_config_file models/uncased_L-12_H-768_A-12/bert_config.json\
 --task_name cla\
 --vocab_file models/uncased_L-12_H-768_A-12/vocab.txt\
 --output_dir outputs/Cla_yu/20_percent_test\
 --init_checkpoint models/uncased_L-12_H-768_A-12/bert_model.ckpt\
 --max_seq_length 256\
 --do_train True\
 --do_eval True\
 --do_predict True\
 --train_batch_size 32\
 --learning_rate 2e-5\
 --num_train_epochs 5.0\
 --gpu 0\
 --cla_nums 12


