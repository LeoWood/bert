:: cscd医学领域数据, max_seq 128, normal

for %%i in (data/cscd_all/*.txt) do python create_pretraining_data.py ^
--vocab_file models/chinese_L-12_H-768_A-12/vocab.txt ^
--output_file data/cscibert_pre_training/pre_training_R_cscd_128.tfrecord ^
--input_file %%i ^
--max_seq_length 128

