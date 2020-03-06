python run_classifier.py^
 --data_dir=data/data_CSL^
 --bert_config_file=models/chinese_L-12_H-768_A-12/bert_config.json^
 --task_name=pair^
 --vocab_file=models/chinese_L-12_H-768_A-12/vocab.txt^
 --output_dir=outputs/CSL_base^
 --init_checkpoint=models/chinese_L-12_H-768_A-12/bert_model.ckpt^
 --max_seq_length=512^
 --do_train=True^
 --do_predict=True^
 --train_batch_size=8^
 --learning_rate=2e-5^
 --num_train_epochs=3.0^
 --gpu=1^
 --cla_nums=2

