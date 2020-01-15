#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: LiuHuan
# Datetime: 2019/6/21 10:45
from sklearn import metrics
import os
import pandas as pd
import tensorflow as tf

flags = tf.flags

FLAGS = flags.FLAGS

## Required parameters
flags.DEFINE_string(
    "output_dir", None,
    "output results dir")

flags.DEFINE_string(
    "data_dir", None,
    "The input data dir. Should contain the .tsv files (or other data files) "
    "for the task.")


if __name__ == '__main__':
    true_labels = []
    with open(os.path.join(FLAGS.data_dir,'test.tsv'), 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            true_labels.append(int(line.split('\t')[0]))

    results1 = pd.read_csv(os.path.join(FLAGS.output_dir,'mask_test_results.tsv'), sep='\t', names=['0', '1', '2', '3', '4'])
    results2 = pd.read_csv(os.path.join(FLAGS.output_dir,'sen_test_results.tsv'), sep='\t', names=['0', '1', '2', '3', '4'])
    df = results1 + results2
    df.to_csv(os.path.join(FLAGS.output_dir,'test_results.csv'),index=False)
    predictions = []
    for i in range(len(df)):
        a = df.iloc[i].tolist()
        predictions.append(a.index(max(a)))
    report = metrics.classification_report(y_true=true_labels,
                                           y_pred=predictions,
                                           labels=[4, 0, 1, 2, 3],
                                           target_names=['Background', 'Objective', 'Methods', 'Results',
                                                         'Conclusions'], digits=4)
    confution_matrix = metrics.confusion_matrix(y_true=true_labels,
                                                y_pred=predictions, labels=[4, 3, 1, 0, 2])
    print(report)
    print(confution_matrix)
    with open(os.path.join(FLAGS.output_dir, "eval_report.txt"), 'w', encoding='utf-8') as f:
        f.write(report)