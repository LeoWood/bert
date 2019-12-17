::Pre1_cscd_R_128_from_scrach 128
python run_pretraining.py^
 --input_file data/cscibert_pre_training/pre_training_R_cscd_128.tfrecord^
 --bert_config_file models/chinese_L-12_H-768_A-12/bert_config.json^
 --output_dir outputs/Pre1_cscd_R_128_from_scrach^
 --max_seq_length 128^
 --do_train True^
 --train_batch_size 32^
 --learning_rate 2e-5^
 --num_train_steps 1000000^
 --gpu 0^

