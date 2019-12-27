:: cla 1000 pre_from_bert 25w steps
python run_classifier.py^
 --data_dir data/data_wanfang_16000^
 --bert_config_file models/chinese_L-12_H-768_A-12/bert_config.json^
 --task_name cla^
 --vocab_file models/chinese_L-12_H-768_A-12/vocab.txt^
 --output_dir outputs/Eval_data16000_pre_from_bert_80w^
 --init_checkpoint outputs/Pre2_cscd_R_128_from_bert/model.ckpt-800000^
 --max_seq_length 400^
 --do_train True^
 --do_predict True^
 --train_batch_size 8^
 --learning_rate 2e-5^
 --num_train_epochs 2.0^
 --gpu 0^
 --cla_nums 16

