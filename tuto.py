# pylint: skip-file

import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def tuto1():
    NODE1 = tf.constant(3.0, tf.float32)
    NODE2 = tf.constant(4.0)
    NODE3 = tf.add(NODE1, NODE2)

    sess = tf.Session()
    print sess.run([NODE1, NODE2, NODE3])

    a = tf.placeholder(tf.float32)
    b = tf.placeholder(tf.float32)
    adder_node = a + b

    print(sess.run(adder_node, {a: 3, b:4.5}))
    print(sess.run(adder_node, {a: [1,3], b: [2.0, 4.5]}))

    return

def tuto2():
    sess = tf.Session()
    # MODEL
    W = tf.Variable([.3], tf.float32)
    b = tf.Variable([-.3], tf.float32)
    x = tf.placeholder(tf.float32)
    linear_model = W * x + b

    init = tf.global_variables_initializer()
    sess.run(init)
    print(sess.run(linear_model, {x:[1,2,3,4]}))

    # LOSS
    y = tf.placeholder(tf.float32)
    squared_deltas = tf.square(linear_model - y)
    loss = tf.reduce_sum(squared_deltas)
    print(sess.run(loss, {x:[1,2,3,4], y:[0,-1,-2,-3]}))

    # TRAIN
    optimizer = tf.train.GradientDescentOptimizer(0.01)
    train = optimizer.minimize(loss)
    for i in range(1000):
        sess.run(train, {x:[1,2,3,4], y:[0,-1,-2,-3]})

    print(sess.run([W, b]))
    return

tuto2()