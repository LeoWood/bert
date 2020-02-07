
python create_ernie_pretraining_data.py ^
 --vocab_file models/chinese_L-12_H-768_A-12/vocab.txt ^
 --output_file data/cscd_new/pre_training_R_cscd_128_wwm_cmesh.tfrecord ^
 --input_file data/cscd_new/R.txt ^
 --max_seq_length 128