python run_classifier.py\
 --data_dir data/xiandao/shandi\
 --bert_config_file models/uncased_L-12_H-768_A-12/bert_config.json\
 --task_name cla\
 --vocab_file models/uncased_L-12_H-768_A-12/vocab.txt\
 --output_dir outputs/Cla_xiandao_tshandi\
 --init_checkpoint models/uncased_L-12_H-768_A-12/bert_model.ckpt\
 --max_seq_length 200\
 --do_train True\
 --do_eval True\
 --do_predict True\
 --train_batch_size 20\
 --learning_rate 2e-5\
 --num_train_epochs 3.0\
 --gpu 0\
 --cla_nums 11

 python run_classifier.py\
 --data_dir data/xiandao/kongjian\
 --bert_config_file models/uncased_L-12_H-768_A-12/bert_config.json\
 --task_name cla\
 --vocab_file models/uncased_L-12_H-768_A-12/vocab.txt\
 --output_dir outputs/Cla_xiandao_kongjian\
 --init_checkpoint models/uncased_L-12_H-768_A-12/bert_model.ckpt\
 --max_seq_length 200\
 --do_train True\
 --do_eval True\
 --do_predict True\
 --train_batch_size 20\
 --learning_rate 2e-5\
 --num_train_epochs 3.0\
 --gpu 0\
 --cla_nums 30

python run_classifier.py\
 --data_dir data/xiandao/tu\
 --bert_config_file models/uncased_L-12_H-768_A-12/bert_config.json\
 --task_name cla\
 --vocab_file models/uncased_L-12_H-768_A-12/vocab.txt\
 --output_dir outputs/Cla_xiandao_tu\
 --init_checkpoint models/uncased_L-12_H-768_A-12/bert_model.ckpt\
 --max_seq_length 200\
 --do_train True\
 --do_eval True\
 --do_predict True\
 --train_batch_size 20\
 --learning_rate 2e-5\
 --num_train_epochs 3.0\
 --gpu 0\
 --cla_nums 17




