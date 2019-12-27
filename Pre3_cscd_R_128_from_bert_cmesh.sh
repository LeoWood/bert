# Pre2_cscd_R_128_from_bert 128
python run_pretraining.py\
 --input_file=data/cscibert_pre_training/pre_training_R_cscd_128_wwm_cmesh.tfrecord\
 --bert_config_file=models/chinese_L-12_H-768_A-12/bert_config.json\
 --init_checkpoint=models/chinese_L-12_H-768_A-12/bert_model.ckpt\
 --output_dir=outputs/Pre3_cscd_R_128_from_bert_wwm_cmesh\
 --max_seq_length=128\
 --do_train=True\
 --do_eval=True\
 --train_batch_size=32\
 --learning_rate=2e-5\
 --num_train_steps=500000\
 --save_checkpoints_steps=100000\
 --gpu=1^

