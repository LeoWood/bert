:: cscd医学领域数据, max_seq 128, cmesh wwm

python create_ernie_pretraining_data.py ^
 --vocab_file models/chinese_L-12_H-768_A-12/vocab.txt ^
 --output_file data/cscd_all_cmesh/pre_training_TP_cscd_128_wwm_cmesh.tfrecord ^
 --input_file data/cscd_all/TP.txt ^
 --max_seq_length 128
python create_ernie_pretraining_data.py ^
 --vocab_file models/chinese_L-12_H-768_A-12/vocab.txt ^
 --output_file data/cscd_all_cmesh/pre_training_TQ_cscd_128_wwm_cmesh.tfrecord ^
 --input_file data/cscd_all/TQ.txt ^
 --max_seq_length 128
python create_ernie_pretraining_data.py ^
 --vocab_file models/chinese_L-12_H-768_A-12/vocab.txt ^
 --output_file data/cscd_all_cmesh/pre_training_TS_cscd_128_wwm_cmesh.tfrecord ^
 --input_file data/cscd_all/TS.txt ^
 --max_seq_length 128
python create_ernie_pretraining_data.py ^
 --vocab_file models/chinese_L-12_H-768_A-12/vocab.txt ^
 --output_file data/cscd_all_cmesh/pre_training_TU_cscd_128_wwm_cmesh.tfrecord ^
 --input_file data/cscd_all/TU.txt ^
 --max_seq_length 128
python create_ernie_pretraining_data.py ^
 --vocab_file models/chinese_L-12_H-768_A-12/vocab.txt ^
 --output_file data/cscd_all_cmesh/pre_training_TV_cscd_128_wwm_cmesh.tfrecord ^
 --input_file data/cscd_all/TV.txt ^
 --max_seq_length 128

