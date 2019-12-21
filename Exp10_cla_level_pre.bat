:: cla level pre_from_bert 25w steps
python run_classifier.py^
 --data_dir data/cla_cscd_level_new^
 --bert_config_file models/chinese_L-12_H-768_A-12/bert_config.json^
 --task_name cla^
 --vocab_file models/chinese_L-12_H-768_A-12/vocab.txt^
 --output_dir outputs/Exp10_cla_cscd_level_pre^
 --init_checkpoint outputs/Pre2_cscd_R_128_from_bert/model.ckpt-250000^
 --max_seq_length 400^
 --do_train True^
 --train_batch_size 8^
 --learning_rate 2e-5^
 --num_train_epochs 2.0^
 --gpu 0^
 --cla_nums 81

