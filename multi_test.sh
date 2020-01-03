#!/bin/bash
#export LD_LIBRARY_PATH=/public/software/deeplearning/tensorflow/openssl-1.1.0j/lib/:$LD_LIBRARY_PATH
export MIOPEN_USER_DB_PATH=/tmp/tensorflow-miopen-2.8
export MIOPEN_DEBUG_DISABLE_FIND_DB=1
export HOROVOD_HIERARCHICAL_ALLREDUCE=1

lrank=$OMPI_COMM_WORLD_LOCAL_RANK


APP="/public/software/deeplearning/anaconda3/bin/python3 run_classifier_gpus.py --data_dir=data/data_wanfang_16000  --bert_config_file=/public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/bert_config.json  --task_name=cla  --vocab_file=/public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/vocab.txt  --output_dir=/public/home/zzx6320/lh/Projects/bert/outputs/test_multi_data_16000  --init_checkpoint=/public/home/zzx6320/lh/Projects/bert/models/chinese_L-12_H-768_A-12/chinese_L-12_H-768_A-12/bert_model.ckpt  --max_seq_length=400  --do_train=True  --do_predict=True  --train_batch_size=8  --learning_rate=2e-5 --num_train_epochs=2.0 --cla_nums=16"

case ${lrank} in
[0])
  export HIP_VISIBLE_DEVICES=0,1,2,3
  export MIOPEN_USER_DB_PATH=/tmp/tensorflow-miopen-${USER}-2.8_0
  numactl --cpunodebind=0 --membind=0 ${APP}
  ;;
[1])
  export HIP_VISIBLE_DEVICES=0,1,2,3
  export MIOPEN_USER_DB_PATH=/tmp/tensorflow-miopen-${USER}-2.8_1
  numactl --cpunodebind=1 --membind=1 ${APP}
  ;;
[2])
  export HIP_VISIBLE_DEVICES=0,1,2,3
  export MIOPEN_USER_DB_PATH=/tmp/tensorflow-miopen-${USER}-2.8_2
  numactl --cpunodebind=2 --membind=2 ${APP}
  ;;
[3])
  export HIP_VISIBLE_DEVICES=0,1,2,3
  export MIOPEN_USER_DB_PATH=/tmp/tensorflow-miopen-${USER}-2.8_3
  numactl --cpunodebind=3 --membind=3 ${APP}
  ;;
esac
