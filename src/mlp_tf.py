# %%
from random import random

import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

# %%


def generate_dataset(num_samples, test_size=0.33):
    """Generates train/test dataset for sum operation

    Args:
        num_samples (int): Num of total samples in dataset
        test_size (float, optional): ratio of output/num_samples.
            Defaults to 0.33.

    Returns:
        x_train: 2d array with input data for training
        x_test: 2d array with input data for testing
        y_train: 2d array with target data for training
        y_test: 2d array with target data for testing
    """

    # build inputs/targets for sum operation: y[0][0] = x[0][0] + x[0][1]
    x = np.array([[random() / 2 for _ in range(2)]
                  for _ in range(num_samples)])
    y = np.array([[i[0] + i[1]] for i in x])

    # split dataset into test and training sets
    x_train, x_test, y_train, y_test = train_test_split(x,
                                                        y,
                                                        test_size=test_size)

    return x_train, x_test, y_train, y_test


# %%
# create a dataset with 2000 samples
x_train, x_test, y_train, y_test = generate_dataset(5000, 0.3)

# %%
# build model with 3 layers: 2 -> 5 -> 1
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(5, input_dim=2, activation="sigmoid"),
    tf.keras.layers.Dense(1, activation="sigmoid"),
])

# %%
# choose optimizer
optimizer = tf.keras.optimizers.SGD(learning_rate=0.1)

# %%
# compile model
model.compile(optimizer=optimizer, loss="mse")

# %%
# train model
model.fit(x_train, y_train, batch_size=1, epochs=100)

# %%
# evaluate model on test set
print("\nEvaluation on the test set:")
model.evaluate(x_train, y_train, batch_size=1, verbose=1)

# %%
data = np.array([[0.1, 0.2], [0.2, 0.2]])
predictions = model.predict(data)
print("\nSome Predictions:")
for d, p in zip(data, predictions):
    print("{} + {} = {}".format(d[0], d[1], p[0]))
