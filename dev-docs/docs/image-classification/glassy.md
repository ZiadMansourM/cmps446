---
sidebar_position: 2
id: Mr. Glassy the Bot
description: NN for Handwritten digit recognition.
slug: /image-classification/glassy
---

import ImagesTable from "../../src/components/ImagesTable";
import CustomImagesTable from "../../src/components/CustomImagesTable";

![mr-glassy](/assets/datasets/minst/glassy.png)

## Prerequisites
This projects assumes that you covered the following concepts beforehand:
- [X] [What does Image Classification mean?](https://pyimagesearch.com/2021/04/17/image-classification-basics/)
- [X] [What are Neural Networks?](https://youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&si=ZR2rxvVOAf8aW3A1)

## MNIST digits dataset
This is a [dataset](https://keras.io/api/datasets/mnist/) of 60,000 28x28 grayscale images of the 10 digits, along with a test set of 10,000 images. More info can be found at the [MNIST homepage](http://yann.lecun.com/exdb/mnist/).


## Workspace
```bash
ziadh@Ziads-MacBook-Air mnist % tree -L 4 -I ".git|.venv|.DS_Store|__pycache__"
.
├── README.md
├── assets
│   └── imgs
│       └── glassy.png
├── data
│   ├── confusion-matrices
│   │   └── 4
│   │       ├── test
│   │       └── train
│   ├── datasets
│   │   └── mnist.npz
│   ├── models
│   │   ├── 20
│   │   │   ├── mnist-20-97.59.model
│   │   │   └── mnist-20-97.65.model
│   │   ├── 3
│   │   │   ├── mnist-3-97.09.model
│   │   │   └── mnist-3-97.11.model
│   │   ├── 4
│   │   │   ├── mnist-4-97.13.model
│   │   │   ├── mnist-4-97.31.model
│   │   │   ├── mnist-4-97.40.model
│   │   │   ├── mnist-4-97.53.model
│   │   │   └── mnist-4-97.59.model
│   │   ├── 5
│   │   │   └── mnist-5-97.25.model
│   │   └── 9
│   │       ├── mnist-9-97.15.model
│   │       ├── mnist-9-97.41.model
│   │       └── mnist-9-97.57.model
│   └── test
│       ├── 0.png
│       ├── 1.png
│       ├── 2.png
│       ├── 3.png
│       ├── 4.png
│       ├── 5.png
│       ├── 6.png
│       ├── 7.png
│       ├── 8.png
│       └── 9.png
├── logs
│   └── tune.log
└── src
    ├── main.ipynb
    ├── requirements.txt
    ├── train.ipynb
    └── utils
        ├── __init__.py
        └── utils.py

31 directories, 19 files
```


## Visualize Training Dataset
```bash
ziadh@Ziads-MacBook-Air mnist % \
for dir in "$(pwd)/temp/train"/*; do
    label=$(basename "$dir")
    count=$(find "$dir" -type f -name "*.png" | wc -l)
    echo "\"$label\": $count"
done
"0":     5923
"1":     6742
"2":     5958
"3":     6131
"4":     5842
"5":     5421
"6":     5918
"7":     6265
"8":     5851
"9":     5949
```

### Ones
<ImagesTable
  size={112}
  heading={"Ones Images"}
  dirname={"train"}
  classdigit={"1"}
/>

### Twos
<ImagesTable
  size={112}
  heading={"Twos Images"}
  dirname={"train"}
  classdigit={"2"}
/>

### Threes
<ImagesTable
  size={112}
  heading={"Threes Images"}
  dirname={"train"}
  classdigit={"3"}
/>

### Fours
<ImagesTable
  size={112}
  heading={"Fours Images"}
  dirname={"train"}
  classdigit={"4"}
/>

### Fives
<ImagesTable
  size={112}
  heading={"Fives Images"}
  dirname={"train"}
  classdigit={"5"}
/>

### Sixes
<ImagesTable
  size={112}
  heading={"Sixes Images"}
  dirname={"train"}
  classdigit={"6"}
/>

### Sevens
<ImagesTable
  size={112}
  heading={"Sevens Images"}
  dirname={"train"}
  classdigit={"7"}
/>

### Eights
<ImagesTable
  size={112}
  heading={"Eights Images"}
  dirname={"train"}
  classdigit={"8"}
/>

### Nines 
<ImagesTable
  size={112}
  heading={"Nines Images"}
  dirname={"train"}
  classdigit={"9"}
/>


## Visualize Test Dataset
```bash
ziadh@Ziads-MacBook-Air mnist % \
> for dir in "$(pwd)/temp/test"/*; do
    label=$(basename "$dir")
    count=$(find "$dir" -type f -name "*.png" | wc -l)
    echo "\"$label\": $count"
done
"0":      980
"1":     1135
"2":     1032
"3":     1010
"4":      982
"5":      892
"6":      958
"7":     1028
"8":      974
"9":     1009
```


### Ones

<ImagesTable
  size={112}
  heading={"Ones Images"}
  dirname={"test"}
  classdigit={"1"}
/>

### Twos

<ImagesTable
  size={112}
  heading={"Twos Images"}
  dirname={"test"}
  classdigit={"2"}
/>

### Threes

<ImagesTable
  size={112}
  heading={"Threes Images"}
  dirname={"test"}
  classdigit={"3"}
/>

### Fours

<ImagesTable
  size={112}
  heading={"Fours Images"}
  dirname={"test"}
  classdigit={"4"}
/>

### Fives

<ImagesTable
  size={112}
  heading={"Fives Images"}
  dirname={"test"}
  classdigit={"5"}
/>

### Sixes

<ImagesTable
  size={112}
  heading={"Sixes Images"}
  dirname={"test"}
  classdigit={"6"}
/>

### Sevens

<ImagesTable
  size={112}
  heading={"Sevens Images"}
  dirname={"test"}
  classdigit={"7"}
/>

### Eights

<ImagesTable
  size={112}
  heading={"Eights Images"}
  dirname={"test"}
  classdigit={"8"}
/>

### Nines

<ImagesTable
  size={112}
  heading={"Nines Images"}
  dirname={"test"}
  classdigit={"9"}
/>


## Visualize Wrong Predictions

### Zeros

<CustomImagesTable
  size={112}
  heading="Wrong Predictions"
  dirname="wrong-predictions"
  classdigit="0"
  imagePaths={[
    "0-0000-9.png",
    "0-0001-9.png",
    "0-0002-6.png",
    "0-0003-3.png",
    "0-0004-9.png",
    "0-0005-8.png",
    "0-0006-7.png",
    "0-0007-4.png",
    "0-0008-3.png",
    "0-0009-9.png",
    "0-0010-6.png",
    "0-0011-1.png"
  ]}
/>


### Ones

<CustomImagesTable
  size={112}
  heading="Wrong Predictions"
  dirname="wrong-predictions"
  classdigit="1"
  imagePaths={[
    "1-0000-8.png",
    "1-0003-2.png",
    "1-0006-8.png",
    "1-0009-8.png",
    "1-0001-2.png",
    "1-0004-3.png",
    "1-0007-8.png",
    "1-0010-8.png",
    "1-0002-2.png",
    "1-0005-6.png",
    "1-0008-6.png"
  ]}
/>

### Twos

<CustomImagesTable
  size={112}
  heading="Wrong Predictions"
  dirname="wrong-predictions"
  classdigit="2"
  imagePaths={[
    "2-0000-7.png",
    "2-0009-3.png",
    "2-0018-0.png",
    "2-0027-8.png",
    "2-0036-0.png",
    "2-0001-1.png",
    "2-0010-0.png",
    "2-0019-3.png",
    "2-0028-3.png",
    "2-0037-8.png",
    "2-0002-8.png",
    "2-0011-0.png",
    "2-0020-3.png",
    "2-0029-6.png",
    "2-0038-3.png",
    "2-0003-1.png",
    "2-0012-3.png",
    "2-0021-7.png",
    "2-0030-3.png",
    "2-0039-8.png",
    "2-0004-7.png",
    "2-0013-1.png",
    "2-0022-1.png",
    "2-0031-8.png",
    "2-0040-0.png",
    "2-0005-3.png",
    "2-0014-0.png",
    "2-0023-7.png",
    "2-0032-4.png",
    "2-0006-6.png",
    "2-0015-4.png",
    "2-0024-8.png",
    "2-0033-7.png",
    "2-0007-0.png",
    "2-0016-3.png",
    "2-0025-3.png",
    "2-0034-8.png",
    "2-0008-8.png",
    "2-0017-1.png",
    "2-0026-3.png",
    "2-0035-0.png"
  ]}
/>


### Threes

<CustomImagesTable
  size={112}
  heading="Wrong Predictions"
  dirname="wrong-predictions"
  classdigit="3"
  imagePaths={[
    "3-0000-8.png",
    "3-0006-7.png",
    "3-0012-5.png",
    "3-0018-5.png",
    "3-0024-9.png",
    "3-0001-7.png",
    "3-0007-2.png",
    "3-0013-7.png",
    "3-0019-2.png",
    "3-0025-8.png",
    "3-0002-7.png",
    "3-0008-7.png",
    "3-0014-8.png",
    "3-0020-2.png",
    "3-0026-8.png",
    "3-0003-5.png",
    "3-0009-7.png",
    "3-0015-8.png",
    "3-0021-2.png",
    "3-0004-5.png",
    "3-0010-2.png",
    "3-0016-5.png",
    "3-0022-2.png",
    "3-0005-2.png",
    "3-0011-8.png",
    "3-0017-5.png",
    "3-0023-9.png"
  ]}
/>



### Fours

<CustomImagesTable
  size={112}
  heading="Wrong Predictions"
  dirname="wrong-predictions"
  classdigit="4"
  imagePaths={[
    "4-0000-2.png",
    "4-0005-6.png",
    "4-0010-6.png",
    "4-0015-6.png",
    "4-0020-7.png",
    "4-0001-9.png",
    "4-0006-6.png",
    "4-0011-2.png",
    "4-0016-7.png",
    "4-0021-0.png",
    "4-0002-6.png",
    "4-0007-2.png",
    "4-0012-9.png",
    "4-0017-2.png",
    "4-0022-1.png",
    "4-0003-0.png",
    "4-0008-6.png",
    "4-0013-7.png",
    "4-0018-9.png",
    "4-0004-9.png",
    "4-0009-2.png",
    "4-0014-9.png",
    "4-0019-8.png"
  ]}
/>


### Fives

<CustomImagesTable
  size={112}
  heading="Wrong Predictions"
  dirname="wrong-predictions"
  classdigit="5"
  imagePaths={[
    "5-0000-3.png",
    "5-0007-6.png",
    "5-0014-3.png",
    "5-0021-3.png",
    "5-0028-3.png",
    "5-0001-8.png",
    "5-0008-8.png",
    "5-0015-0.png",
    "5-0022-3.png",
    "5-0029-6.png",
    "5-0002-9.png",
    "5-0009-3.png",
    "5-0016-3.png",
    "5-0023-3.png",
    "5-0030-0.png",
    "5-0003-3.png",
    "5-0010-3.png",
    "5-0017-2.png",
    "5-0024-8.png",
    "5-0031-6.png",
    "5-0004-3.png",
    "5-0011-3.png",
    "5-0018-6.png",
    "5-0025-3.png",
    "5-0032-6.png",
    "5-0005-3.png",
    "5-0012-4.png",
    "5-0019-3.png",
    "5-0026-3.png",
    "5-0006-0.png",
    "5-0013-9.png",
    "5-0020-3.png",
    "5-0027-3.png"
  ]}
/>



### Sixs

<CustomImagesTable
  size={112}
  heading="Wrong Predictions"
  dirname="wrong-predictions"
  classdigit="6"
  imagePaths={[
    "6-0000-0.png",
    "6-0004-0.png",
    "6-0008-0.png",
    "6-0012-2.png",
    "6-0016-5.png",
    "6-0001-0.png",
    "6-0005-1.png",
    "6-0009-4.png",
    "6-0013-0.png",
    "6-0002-5.png",
    "6-0006-1.png",
    "6-0010-5.png",
    "6-0014-4.png",
    "6-0003-1.png",
    "6-0007-4.png",
    "6-0011-2.png",
    "6-0015-3.png"
  ]}
/>


### Sevens

<CustomImagesTable
  size={112}
  heading="Wrong Predictions"
  dirname="wrong-predictions"
  classdigit="7"
  imagePaths={[
    "7-0000-3.png",
    "7-0007-0.png",
    "7-0014-2.png",
    "7-0021-1.png",
    "7-0028-2.png",
    "7-0001-2.png",
    "7-0008-9.png",
    "7-0015-3.png",
    "7-0022-0.png",
    "7-0029-2.png",
    "7-0002-8.png",
    "7-0009-3.png",
    "7-0016-3.png",
    "7-0023-1.png",
    "7-0030-2.png",
    "7-0003-9.png",
    "7-0010-1.png",
    "7-0017-1.png",
    "7-0024-1.png",
    "7-0031-2.png",
    "7-0004-2.png",
    "7-0011-3.png",
    "7-0018-1.png",
    "7-0025-1.png",
    "7-0005-1.png",
    "7-0012-1.png",
    "7-0019-9.png",
    "7-0026-1.png",
    "7-0006-9.png",
    "7-0013-5.png",
    "7-0020-1.png",
    "7-0027-3.png"
  ]}
/>



### Eights

<CustomImagesTable
  size={112}
  heading="Wrong Predictions"
  dirname="wrong-predictions"
  classdigit="8"
  imagePaths={[
    "8-0000-0.png",
    "8-0010-4.png",
    "8-0020-9.png",
    "8-0030-0.png",
    "8-0040-9.png",
    "8-0001-4.png",
    "8-0011-7.png",
    "8-0021-9.png",
    "8-0031-6.png",
    "8-0041-0.png",
    "8-0002-2.png",
    "8-0012-0.png",
    "8-0022-5.png",
    "8-0032-4.png",
    "8-0042-6.png",
    "8-0003-0.png",
    "8-0013-3.png",
    "8-0023-0.png",
    "8-0033-3.png",
    "8-0043-4.png",
    "8-0004-2.png",
    "8-0014-3.png",
    "8-0024-3.png",
    "8-0034-4.png",
    "8-0044-2.png",
    "8-0005-4.png",
    "8-0015-9.png",
    "8-0025-7.png",
    "8-0035-4.png",
    "8-0045-7.png",
    "8-0006-7.png",
    "8-0016-4.png",
    "8-0026-4.png",
    "8-0036-2.png",
    "8-0046-6.png",
    "8-0007-6.png",
    "8-0017-1.png",
    "8-0027-3.png",
    "8-0037-9.png",
    "8-0047-6.png",
    "8-0008-9.png",
    "8-0018-0.png",
    "8-0028-0.png",
    "8-0038-9.png",
    "8-0048-5.png",
    "8-0009-0.png",
    "8-0019-0.png",
    "8-0029-7.png",
    "8-0039-4.png",
    "8-0049-6.png"
  ]}
/>



### Nines

<CustomImagesTable
  size={112}
  heading="Wrong Predictions"
  dirname="wrong-predictions"
  classdigit="9"
  imagePaths={[
    "9-0000-5.png",
    "9-0008-5.png",
    "9-0016-5.png",
    "9-0024-7.png",
    "9-0032-4.png",
    "9-0001-4.png",
    "9-0009-0.png",
    "9-0017-1.png",
    "9-0025-5.png",
    "9-0033-4.png",
    "9-0002-3.png",
    "9-0010-1.png",
    "9-0018-1.png",
    "9-0026-4.png",
    "9-0034-7.png",
    "9-0003-3.png",
    "9-0011-1.png",
    "9-0019-3.png",
    "9-0027-4.png",
    "9-0035-4.png",
    "9-0004-8.png",
    "9-0012-4.png",
    "9-0020-4.png",
    "9-0028-1.png",
    "9-0036-4.png",
    "9-0005-4.png",
    "9-0013-3.png",
    "9-0021-4.png",
    "9-0029-3.png",
    "9-0006-8.png",
    "9-0014-0.png",
    "9-0022-4.png",
    "9-0030-4.png",
    "9-0007-1.png",
    "9-0015-4.png",
    "9-0023-4.png",
    "9-0031-0.png"
  ]}
/>


## Confusion Matrix

<div align="center">

![confusion-matrix](/assets/datasets/minst/confusion-matrices/mnist-train-4-97.17.png)

</div>

## Code

### Imports && Magic Numbers

```python
import os
from pathlib import Path
from typing import Final

import tensorflow as tf

import utils
```

```python
EPOCHS: Final[int] = 4
```


### Load model

```python
utils.log_to_file(f"Training with EPOCHS={EPOCHS}")
```

```python
"""minst.load_data()
Returns:
    - Tuple of NumPy arrays: (x_train, y_train), (x_test, y_test).

    - x_train: uint8 NumPy array of grayscale image data with shapes
    (60000, 28, 28), containing the training data. Pixel values range from 0 to 255.

    - y_train: uint8 NumPy array of digit labels (integers in range 0-9)
    with shape (60000,) for the training data.

    - x_test: uint8 NumPy array of grayscale image data with shapes
    (10000, 28, 28), containing the test data. Pixel values range from 0 to 255.

    - y_test: uint8 NumPy array of digit labels (integers in range 0-9)
    with shape (10000,) for the test data.
"""

minst = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = minst.load_data(path=os.path.join(
    utils.DATA_DIR, 
    "datasets", 
    "mnist.npz"
))
```

```python
assert x_train.shape == (60_000, 28, 28)
assert x_train.dtype == "uint8"

assert y_train.shape == (60_000,)
assert y_train.dtype == "uint8"

assert x_test.shape == (10_000, 28, 28)
assert x_test.dtype == "uint8"

assert y_test.shape == (10_000,)
assert y_test.dtype == "uint8"
```

### Training Model

```python
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)
```

```python
assert x_train.dtype == "float64"
assert x_test.dtype == "float64"
```

```python
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))

model.compile(
    optimizer=tf.keras.optimizers.Adam(), 
    loss=tf.keras.losses.SparseCategoricalCrossentropy(), 
    metrics=['accuracy']
)
```

```python
model.fit(x_train, y_train, epochs=EPOCHS)
```

```python
model.summary()
```

```
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 flatten (Flatten)           (None, 784)               0         
                                                                 
 dense (Dense)               (None, 128)               100480    
                                                                 
 dense_1 (Dense)             (None, 128)               16512     
                                                                 
 dense_2 (Dense)             (None, 10)                1290      
                                                                 
=================================================================
Total params: 118282 (462.04 KB)
Trainable params: 118282 (462.04 KB)
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________
```

```python
val_loss, val_acc = model.evaluate(x_test, y_test)
utils.log_to_file(f"Loss: {val_loss:.4f}, Accuracy: {val_acc*100:.2f}%")
```

```python
model_path: Path = os.path.join(
    utils.DATA_DIR, 
    "models", 
    str(EPOCHS), 
    f"mnist-{EPOCHS}-{val_acc*100:.2f}.model"
)
model.save(model_path)
```

```python
utils.log_to_file(f"Finished training with EPOCHS={EPOCHS}")
utils.log_to_file(f"Model saved to path '{str(model_path)}'")
```

### Calc Confusion Matrix

```python
import numpy as np

y_test_predected: np.ndarray[np.ndarray] = model.predict(x_test)

y_test_predected_labels: list[int] = [
    np.argmax(prediction)
    for prediction in y_test_predected
]

utils.log_to_file(f"False predictions: {sum(y_test_predected_labels != y_test):,}/{len(y_test):,}")
utils.log_to_file(f"True predictions: {sum(y_test_predected_labels == y_test):,}/{len(y_test):,}")
```

```python
confusion_matrix = tf.math.confusion_matrix(
    labels=y_test,
    predictions=y_test_predected_labels
)
```

```python
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt

plt.figure(figsize=(10,7))
sn.heatmap(confusion_matrix, annot=True, fmt='g')

Path(os.path.join(
    utils.DATA_DIR, 
    "confusion-matrices", 
    str(EPOCHS), 
    "train"
)).mkdir(parents=True, exist_ok=True)

confusion_matrix_path: Path = os.path.join(
    utils.DATA_DIR, 
    "confusion-matrices", 
    str(EPOCHS), 
    "train",
    f"mnist-{EPOCHS}-{val_acc*100:.2f}.png"
)
plt.savefig(confusion_matrix_path)
plt.show()

utils.log_to_file(f"Confusion matrix saved to path '{str(confusion_matrix_path)}'")
```

## Extra Custom Test

### Custom Datasets

0 predected 0 | 1 predected 1 | 2 predected 3 | 3 predected 3 | 4 predected 7
:--: | :--: | :--: | :--: | :--:
![zero](/assets/datasets/minst/custom-test/0.png) | ![one](/assets/datasets/minst/custom-test/1.png) | ![two](/assets/datasets/minst/custom-test/2.png) | ![three](/assets/datasets/minst/custom-test/3.png) | ![four](/assets/datasets/minst/custom-test/4.png)


5 predected 5 | 6 predected 5 | 7 predected 1 | 8 predected 3 | 9 predected 3
:--: | :--: | :--: | :--: | :--:
![five](/assets/datasets/minst/custom-test/5.png) | ![six](/assets/datasets/minst/custom-test/6.png) | ![seven](/assets/datasets/minst/custom-test/7.png) | ![eight](/assets/datasets/minst/custom-test/8.png) | ![nine](/assets/datasets/minst/custom-test/9.png)

### Confusion Matrix
![confusion-matrix](/assets/datasets/minst/custom-test/mnist-test-4-97.13.png)

### Wrong Predictions

2 predected 3 | 4 predected 7 | 6 predected 5 
:--: | :--: | :--:
![two](/assets/datasets/minst/custom-test/2.png) | ![four](/assets/datasets/minst/custom-test/4.png) | ![six](/assets/datasets/minst/custom-test/6.png)


| 7 predected 1 | 8 predected 3 | 9 predected 3
:--: | :--: | :--:
![seven](/assets/datasets/minst/custom-test/7.png) | ![eight](/assets/datasets/minst/custom-test/8.png) | ![nine](/assets/datasets/minst/custom-test/9.png)



## Logs
```.log
[2023-10-25 12:26:40] Training with EPOCHS=4
[2023-10-25 12:26:49] Loss: 0.0918, Accuracy: 97.17%
[2023-10-25 12:26:50] Finished training with EPOCHS=4
[2023-10-25 12:26:50] Model saved to path '/Users/ziadh/Desktop/playgroud/image-processing/classifications/mnist/data/models/4/mnist-4-97.17.model'
[2023-10-25 12:26:50] False predictions: 283/10,000
[2023-10-25 12:26:50] True predictions: 9,717/10,000
[2023-10-25 12:26:50] Confusion matrix saved to path '/Users/ziadh/Desktop/playgroud/image-processing/classifications/mnist/data/confusion-matrices/4/train/mnist-4-97.17.png'
[2023-10-25 17:23:24] Testing model with EPOCHS: 4 and ACCURACY: 97.17
[2023-10-25 17:23:24] predected: 3 and it was 8
[2023-10-25 17:23:24] predected: 3 and it was 9
[2023-10-25 17:23:24] predected: 7 and it was 4
[2023-10-25 17:23:24] predected: 5 and it was 5
[2023-10-25 17:23:24] predected: 1 and it was 7
[2023-10-25 17:23:24] predected: 5 and it was 6
[2023-10-25 17:23:24] predected: 3 and it was 2
[2023-10-25 17:23:24] predected: 3 and it was 3
[2023-10-25 17:23:24] predected: 1 and it was 1
[2023-10-25 17:23:24] predected: 0 and it was 0
[2023-10-25 17:23:24] Accuracy: 40.0%
[2023-10-25 17:23:24] Number of faults: 6/10
[2023-10-25 17:23:24] Number of correct: 4/10
```

## Comments
- We can infer from the confusion matrix and comparing pictures of wrong predictions with correct ones that the model would have been more accurate if skeletonization were performed on the images.

> Look up difference between Thinning and skeletonization

## REFERENCES
- [Repository Containing all the work.](https://github.com/ZiadMansourM/glassy)
- [3b1b Neural networks](https://youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&si=ZR2rxvVOAf8aW3A1)
- [Stanford CS231n.](http://cs231n.stanford.edu/)
- [Neural Network Python Project - Handwritten Digit Recognition.](https://youtu.be/bte8Er0QhDg?si=v08WrMPzQmQIQeWE)