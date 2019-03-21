#!/usr/bin/python
#coding=utf-8
#########################################################################
# File Name: test.py
# Author: netease
# Mail: netease@netease.com
# Created Time: Thu 21 Mar 2019 02:36:35 PM CST
# Brief: 
#########################################################################
import tensorflow as tf
import numpy as np

def main():
    def key_func(x):
        # return tf.int64 
        print(x)
        return ds%2

    def reduce_func(key, windowed_data):
        print(key)
        return windowed_data.batch(10)
    
    components = np.arange(100).astype(np.int64)
    dataset = tf.data.Dataset.from_tensor_slices(components)
    dataset = dataset.apply(tf.contrib.data.group_by_window(key_func=key_func, reduce_func=reduce_func_test, window_size=40))
    iterator = dataset.make_one_shot_iterator()
    features = iterator.get_next()
    sess = tf.Session()
    print(sess.run(features))
    print(sess.run(features))

if __name__ == '__main__':
    main()
