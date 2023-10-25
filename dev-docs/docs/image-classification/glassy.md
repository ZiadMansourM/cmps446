---
sidebar_position: 1
id: Mr. Glassy the Bot
description: NN for Handwritten digit recognition.
slug: /image-classification/glassy
---

export const ImagesTable = ({ first, second, third, fourth, heading, size }) => (
  <div style={{ display: 'inline-block' }}>
    <table>
      <tbody>
        <tr>
          <td colSpan={8} style={{ textAlign: 'center' }}>
            {heading}
          </td>
        </tr>
        <tr>
          {first.map((imageSrc, index) => (
            <td key={index}>
              <img src={`/assets/datasets/minst/${imageSrc}`} width={size} height={size} />
            </td>
          ))}
        </tr>
        <tr>
          {second.map((imageSrc, index) => (
            <td key={index}>
              <img src={`/assets/datasets/minst/${imageSrc}`} width={size} height={size} />
            </td>
          ))}
        </tr>
        <tr>
          {third.map((imageSrc, index) => (
            <td key={index}>
              <img src={`/assets/datasets/minst/${imageSrc}`} width={size} height={size} />
            </td>
          ))}
        </tr>
        <tr>
          {fourth.map((imageSrc, index) => (
            <td key={index}>
              <img src={`/assets/datasets/minst/${imageSrc}`} width={size} height={size} />
            </td>
          ))}
        </tr>
      </tbody>
    </table>
  </div>
);


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

### Zeros

<ImagesTable
  size={112}
  heading={"Zeros Images"}
  first={[
    "train/0/0-0000.png",
    "train/0/0-0001.png",
    "train/0/0-0002.png",
    "train/0/0-0003.png",
    "train/0/0-0004.png",
    "train/0/0-0005.png",
    "train/0/0-0006.png",
    "train/0/0-0007.png",
  ]}
  second={[
    "train/0/0-0008.png",
    "train/0/0-0009.png",
    "train/0/0-0010.png",
    "train/0/0-0011.png",
    "train/0/0-0012.png",
    "train/0/0-0013.png",
    "train/0/0-0014.png",
    "train/0/0-0015.png",
  ]}
  third={[
    "train/0/0-0016.png",
    "train/0/0-0017.png",
    "train/0/0-0018.png",
    "train/0/0-0019.png",
    "train/0/0-0020.png",
    "train/0/0-0021.png",
    "train/0/0-0022.png",
    "train/0/0-0023.png",
  ]}
  fourth={[
    "train/0/0-0024.png",
    "train/0/0-0025.png",
    "train/0/0-0026.png",
    "train/0/0-0027.png",
    "train/0/0-0028.png",
    "train/0/0-0029.png",
    "train/0/0-0030.png",
    "train/0/0-0031.png",
  ]}
/>

### Ones

<ImagesTable
    size={112}
    heading={"Ones Images"}
    first={[
        "train/1/1-0000.png",
        "train/1/1-0001.png",
        "train/1/1-0002.png",
        "train/1/1-0003.png",
        "train/1/1-0004.png",
        "train/1/1-0005.png",
        "train/1/1-0006.png",
        "train/1/1-0007.png",
    ]}
    second={[
        "train/1/1-0008.png",
        "train/1/1-0009.png",
        "train/1/1-0010.png",
        "train/1/1-0011.png",
        "train/1/1-0012.png",
        "train/1/1-0013.png",
        "train/1/1-0014.png",
        "train/1/1-0015.png",
    ]}
    third={[
        "train/1/1-0016.png",
        "train/1/1-0017.png",
        "train/1/1-0018.png",
        "train/1/1-0019.png",
        "train/1/1-0020.png",
        "train/1/1-0021.png",
        "train/1/1-0022.png",
        "train/1/1-0023.png",
    ]}
    fourth={[
        "train/1/1-0024.png",
        "train/1/1-0025.png",
        "train/1/1-0026.png",
        "train/1/1-0027.png",
        "train/1/1-0028.png",
        "train/1/1-0029.png",
        "train/1/1-0030.png",
        "train/1/1-0031.png",
    ]}
/>

### Twos

<ImagesTable
    size={112}
    heading={"Twos Images"}
    first={[
        "train/2/2-0000.png",
        "train/2/2-0001.png",
        "train/2/2-0002.png",
        "train/2/2-0003.png",
        "train/2/2-0004.png",
        "train/2/2-0005.png",
        "train/2/2-0006.png",
        "train/2/2-0007.png",
    ]}
    second={[
        "train/2/2-0008.png",
        "train/2/2-0009.png",
        "train/2/2-0010.png",
        "train/2/2-0011.png",
        "train/2/2-0012.png",
        "train/2/2-0013.png",
        "train/2/2-0014.png",
        "train/2/2-0015.png",
    ]}
    third={[
        "train/2/2-0016.png",
        "train/2/2-0017.png",
        "train/2/2-0018.png",
        "train/2/2-0019.png",
        "train/2/2-0020.png",
        "train/2/2-0021.png",
        "train/2/2-0022.png",
        "train/2/2-0023.png",
    ]}
    fourth={[
        "train/2/2-0024.png",
        "train/2/2-0025.png",
        "train/2/2-0026.png",
        "train/2/2-0027.png",
        "train/2/2-0028.png",
        "train/2/2-0029.png",
        "train/2/2-0030.png",
        "train/2/2-0031.png",
    ]}
/>


### Threes

<ImagesTable
    size={112}
    heading={"Threes Images"}
    first={[
        "train/3/3-0000.png",
        "train/3/3-0001.png",
        "train/3/3-0002.png",
        "train/3/3-0003.png",
        "train/3/3-0004.png",
        "train/3/3-0005.png",
        "train/3/3-0006.png",
        "train/3/3-0007.png",
    ]}
    second={[
        "train/3/3-0008.png",
        "train/3/3-0009.png",
        "train/3/3-0010.png",
        "train/3/3-0011.png",
        "train/3/3-0012.png",
        "train/3/3-0013.png",
        "train/3/3-0014.png",
        "train/3/3-0015.png",
    ]}
    third={[
        "train/3/3-0016.png",
        "train/3/3-0017.png",
        "train/3/3-0018.png",
        "train/3/3-0019.png",
        "train/3/3-0020.png",
        "train/3/3-0021.png",
        "train/3/3-0022.png",
        "train/3/3-0023.png",
    ]}
    fourth={[
        "train/3/3-0024.png",
        "train/3/3-0025.png",
        "train/3/3-0026.png",
        "train/3/3-0027.png",
        "train/3/3-0028.png",
        "train/3/3-0029.png",
        "train/3/3-0030.png",
        "train/3/3-0031.png",
    ]}
/>

### Fours

<ImagesTable
    size={112}
    heading={"Fours Images"}
    first={[
        "train/4/4-0000.png",
        "train/4/4-0001.png",
        "train/4/4-0002.png",
        "train/4/4-0003.png",
        "train/4/4-0004.png",
        "train/4/4-0005.png",
        "train/4/4-0006.png",
        "train/4/4-0007.png",
    ]}
    second={[
        "train/4/4-0008.png",
        "train/4/4-0009.png",
        "train/4/4-0010.png",
        "train/4/4-0011.png",
        "train/4/4-0012.png",
        "train/4/4-0013.png",
        "train/4/4-0014.png",
        "train/4/4-0015.png",
    ]}
    third={[
        "train/4/4-0016.png",
        "train/4/4-0017.png",
        "train/4/4-0018.png",
        "train/4/4-0019.png",
        "train/4/4-0020.png",
        "train/4/4-0021.png",
        "train/4/4-0022.png",
        "train/4/4-0023.png",
    ]}
    fourth={[
        "train/4/4-0024.png",
        "train/4/4-0025.png",
        "train/4/4-0026.png",
        "train/4/4-0027.png",
        "train/4/4-0028.png",
        "train/4/4-0029.png",
        "train/4/4-0030.png",
        "train/4/4-0031.png",
    ]}
/>

### Fives

<ImagesTable
    size={112}
    heading={"Fives Images"}
    first={[
        "train/5/5-0000.png",
        "train/5/5-0001.png",
        "train/5/5-0002.png",
        "train/5/5-0003.png",
        "train/5/5-0004.png",
        "train/5/5-0005.png",
        "train/5/5-0006.png",
        "train/5/5-0007.png",
    ]}
    second={[
        "train/5/5-0008.png",
        "train/5/5-0009.png",
        "train/5/5-0010.png",
        "train/5/5-0011.png",
        "train/5/5-0012.png",
        "train/5/5-0013.png",
        "train/5/5-0014.png",
        "train/5/5-0015.png",
    ]}
    third={[
        "train/5/5-0016.png",
        "train/5/5-0017.png",
        "train/5/5-0018.png",
        "train/5/5-0019.png",
        "train/5/5-0020.png",
        "train/5/5-0021.png",
        "train/5/5-0022.png",
        "train/5/5-0023.png",
    ]}
    fourth={[
        "train/5/5-0024.png",
        "train/5/5-0025.png",
        "train/5/5-0026.png",
        "train/5/5-0027.png",
        "train/5/5-0028.png",
        "train/5/5-0029.png",
        "train/5/5-0030.png",
        "train/5/5-0031.png",
    ]}
/>

### Sixes

<ImagesTable
    size={112}
    heading={"Sixes Images"}
    first={[
        "train/6/6-0000.png",
        "train/6/6-0001.png",
        "train/6/6-0002.png",
        "train/6/6-0003.png",
        "train/6/6-0004.png",
        "train/6/6-0005.png",
        "train/6/6-0006.png",
        "train/6/6-0007.png",
    ]}
    second={[
        "train/6/6-0008.png",
        "train/6/6-0009.png",
        "train/6/6-0010.png",
        "train/6/6-0011.png",
        "train/6/6-0012.png",
        "train/6/6-0013.png",
        "train/6/6-0014.png",
        "train/6/6-0015.png",
    ]}
    third={[
        "train/6/6-0016.png",
        "train/6/6-0017.png",
        "train/6/6-0018.png",
        "train/6/6-0019.png",
        "train/6/6-0020.png",
        "train/6/6-0021.png",
        "train/6/6-0022.png",
        "train/6/6-0023.png",
    ]}
    fourth={[
        "train/6/6-0024.png",
        "train/6/6-0025.png",
        "train/6/6-0026.png",
        "train/6/6-0027.png",
        "train/6/6-0028.png",
        "train/6/6-0029.png",
        "train/6/6-0030.png",
        "train/6/6-0031.png",
    ]}
/>

### Sevens

<ImagesTable
    size={112}
    heading={"Sevens Images"}
    first={[
        "train/7/7-0000.png",
        "train/7/7-0001.png",
        "train/7/7-0002.png",
        "train/7/7-0003.png",
        "train/7/7-0004.png",
        "train/7/7-0005.png",
        "train/7/7-0006.png",
        "train/7/7-0007.png",
    ]}
    second={[
        "train/7/7-0008.png",
        "train/7/7-0009.png",
        "train/7/7-0010.png",
        "train/7/7-0011.png",
        "train/7/7-0012.png",
        "train/7/7-0013.png",
        "train/7/7-0014.png",
        "train/7/7-0015.png",
    ]}
    third={[
        "train/7/7-0016.png",
        "train/7/7-0017.png",
        "train/7/7-0018.png",
        "train/7/7-0019.png",
        "train/7/7-0020.png",
        "train/7/7-0021.png",
        "train/7/7-0022.png",
        "train/7/7-0023.png",
    ]}
    fourth={[
        "train/7/7-0024.png",
        "train/7/7-0025.png",
        "train/7/7-0026.png",
        "train/7/7-0027.png",
        "train/7/7-0028.png",
        "train/7/7-0029.png",
        "train/7/7-0030.png",
        "train/7/7-0031.png",
    ]}
/>

### Eights

<ImagesTable
    size={112}
    heading={"Eights Images"}
    first={[
        "train/8/8-0000.png",
        "train/8/8-0001.png",
        "train/8/8-0002.png",
        "train/8/8-0003.png",
        "train/8/8-0004.png",
        "train/8/8-0005.png",
        "train/8/8-0006.png",
        "train/8/8-0007.png",
    ]}
    second={[
        "train/8/8-0008.png",
        "train/8/8-0009.png",
        "train/8/8-0010.png",
        "train/8/8-0011.png",
        "train/8/8-0012.png",
        "train/8/8-0013.png",
        "train/8/8-0014.png",
        "train/8/8-0015.png",
    ]}
    third={[
        "train/8/8-0016.png",
        "train/8/8-0017.png",
        "train/8/8-0018.png",
        "train/8/8-0019.png",
        "train/8/8-0020.png",
        "train/8/8-0021.png",
        "train/8/8-0022.png",
        "train/8/8-0023.png",
    ]}
    fourth={[
        "train/8/8-0024.png",
        "train/8/8-0025.png",
        "train/8/8-0026.png",
        "train/8/8-0027.png",
        "train/8/8-0028.png",
        "train/8/8-0029.png",
        "train/8/8-0030.png",
        "train/8/8-0031.png",
    ]}
/>

### Nines

<ImagesTable
    size={112}
    heading={"Nines Images"}
    first={[
        "train/9/9-0000.png",
        "train/9/9-0001.png",
        "train/9/9-0002.png",
        "train/9/9-0003.png",
        "train/9/9-0004.png",
        "train/9/9-0005.png",
        "train/9/9-0006.png",
        "train/9/9-0007.png",
    ]}
    second={[
        "train/9/9-0008.png",
        "train/9/9-0009.png",
        "train/9/9-0010.png",
        "train/9/9-0011.png",
        "train/9/9-0012.png",
        "train/9/9-0013.png",
        "train/9/9-0014.png",
        "train/9/9-0015.png",
    ]}
    third={[
        "train/9/9-0016.png",
        "train/9/9-0017.png",
        "train/9/9-0018.png",
        "train/9/9-0019.png",
        "train/9/9-0020.png",
        "train/9/9-0021.png",
        "train/9/9-0022.png",
        "train/9/9-0023.png",
    ]}
    fourth={[
        "train/9/9-0024.png",
        "train/9/9-0025.png",
        "train/9/9-0026.png",
        "train/9/9-0027.png",
        "train/9/9-0028.png",
        "train/9/9-0029.png",
        "train/9/9-0030.png",
        "train/9/9-0031.png",
    ]}
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

### Zeros
<ImagesTable
    size={112}
    heading={"Zeros Images"}
    first={[
        "test/0/0-0000.png",
        "test/0/0-0001.png",
        "test/0/0-0002.png",
        "test/0/0-0003.png",
        "test/0/0-0004.png",
        "test/0/0-0005.png",
        "test/0/0-0006.png",
        "test/0/0-0007.png",
    ]}
    second={[
        "test/0/0-0008.png",
        "test/0/0-0009.png",
        "test/0/0-0010.png",
        "test/0/0-0011.png",
        "test/0/0-0012.png",
        "test/0/0-0013.png",
        "test/0/0-0014.png",
        "test/0/0-0015.png",
    ]}
    third={[
        "test/0/0-0016.png",
        "test/0/0-0017.png",
        "test/0/0-0018.png",
        "test/0/0-0019.png",
        "test/0/0-0020.png",
        "test/0/0-0021.png",
        "test/0/0-0022.png",
        "test/0/0-0023.png",
    ]}
    fourth={[
        "test/0/0-0024.png",
        "test/0/0-0025.png",
        "test/0/0-0026.png",
        "test/0/0-0027.png",
        "test/0/0-0028.png",
        "test/0/0-0029.png",
        "test/0/0-0030.png",
        "test/0/0-0031.png",
    ]}
/>

### Ones

<ImagesTable
    size={112}
    heading={"Ones Images"}
    first={[
        "test/1/1-0000.png",
        "test/1/1-0001.png",
        "test/1/1-0002.png",
        "test/1/1-0003.png",
        "test/1/1-0004.png",
        "test/1/1-0005.png",
        "test/1/1-0006.png",
        "test/1/1-0007.png",
    ]}
    second={[
        "test/1/1-0008.png",
        "test/1/1-0009.png",
        "test/1/1-0010.png",
        "test/1/1-0011.png",
        "test/1/1-0012.png",
        "test/1/1-0013.png",
        "test/1/1-0014.png",
        "test/1/1-0015.png",
    ]}
    third={[
        "test/1/1-0016.png",
        "test/1/1-0017.png",
        "test/1/1-0018.png",
        "test/1/1-0019.png",
        "test/1/1-0020.png",
        "test/1/1-0021.png",
        "test/1/1-0022.png",
        "test/1/1-0023.png",
    ]}
    fourth={[
        "test/1/1-0024.png",
        "test/1/1-0025.png",
        "test/1/1-0026.png",
        "test/1/1-0027.png",
        "test/1/1-0028.png",
        "test/1/1-0029.png",
        "test/1/1-0030.png",
        "test/1/1-0031.png",
    ]}
/>

### Twos

<ImagesTable
    size={112}
    heading={"Twos Images"}
    first={[
        "test/2/2-0000.png",
        "test/2/2-0001.png",
        "test/2/2-0002.png",
        "test/2/2-0003.png",
        "test/2/2-0004.png",
        "test/2/2-0005.png",
        "test/2/2-0006.png",
        "test/2/2-0007.png",
    ]}
    second={[
        "test/2/2-0008.png",
        "test/2/2-0009.png",
        "test/2/2-0010.png",
        "test/2/2-0011.png",
        "test/2/2-0012.png",
        "test/2/2-0013.png",
        "test/2/2-0014.png",
        "test/2/2-0015.png",
    ]}
    third={[
        "test/2/2-0016.png",
        "test/2/2-0017.png",
        "test/2/2-0018.png",
        "test/2/2-0019.png",
        "test/2/2-0020.png",
        "test/2/2-0021.png",
        "test/2/2-0022.png",
        "test/2/2-0023.png",
    ]}
    fourth={[
        "test/2/2-0024.png",
        "test/2/2-0025.png",
        "test/2/2-0026.png",
        "test/2/2-0027.png",
        "test/2/2-0028.png",
        "test/2/2-0029.png",
        "test/2/2-0030.png",
        "test/2/2-0031.png",
    ]}
/>

### Threes

<ImagesTable
    size={112}
    heading={"Threes Images"}
    first={[
        "test/3/3-0000.png",
        "test/3/3-0001.png",
        "test/3/3-0002.png",
        "test/3/3-0003.png",
        "test/3/3-0004.png",
        "test/3/3-0005.png",
        "test/3/3-0006.png",
        "test/3/3-0007.png",
    ]}
    second={[
        "test/3/3-0008.png",
        "test/3/3-0009.png",
        "test/3/3-0010.png",
        "test/3/3-0011.png",
        "test/3/3-0012.png",
        "test/3/3-0013.png",
        "test/3/3-0014.png",
        "test/3/3-0015.png",
    ]}
    third={[
        "test/3/3-0016.png",
        "test/3/3-0017.png",
        "test/3/3-0018.png",
        "test/3/3-0019.png",
        "test/3/3-0020.png",
        "test/3/3-0021.png",
        "test/3/3-0022.png",
        "test/3/3-0023.png",
    ]}
    fourth={[
        "test/3/3-0024.png",
        "test/3/3-0025.png",
        "test/3/3-0026.png",
        "test/3/3-0027.png",
        "test/3/3-0028.png",
        "test/3/3-0029.png",
        "test/3/3-0030.png",
        "test/3/3-0031.png",
    ]}
/>

### Fours

<ImagesTable
    size={112}
    heading={"Fours Images"}
    first={[
        "test/4/4-0000.png",
        "test/4/4-0001.png",
        "test/4/4-0002.png",
        "test/4/4-0003.png",
        "test/4/4-0004.png",
        "test/4/4-0005.png",
        "test/4/4-0006.png",
        "test/4/4-0007.png",
    ]}
    second={[
        "test/4/4-0008.png",
        "test/4/4-0009.png",
        "test/4/4-0010.png",
        "test/4/4-0011.png",
        "test/4/4-0012.png",
        "test/4/4-0013.png",
        "test/4/4-0014.png",
        "test/4/4-0015.png",
    ]}
    third={[
        "test/4/4-0016.png",
        "test/4/4-0017.png",
        "test/4/4-0018.png",
        "test/4/4-0019.png",
        "test/4/4-0020.png",
        "test/4/4-0021.png",
        "test/4/4-0022.png",
        "test/4/4-0023.png",
    ]}
    fourth={[
        "test/4/4-0024.png",
        "test/4/4-0025.png",
        "test/4/4-0026.png",
        "test/4/4-0027.png",
        "test/4/4-0028.png",
        "test/4/4-0029.png",
        "test/4/4-0030.png",
        "test/4/4-0031.png",
    ]}
/>

### Fives

<ImagesTable
    size={112}
    heading={"Fives Images"}
    first={[
        "test/5/5-0000.png",
        "test/5/5-0001.png",
        "test/5/5-0002.png",
        "test/5/5-0003.png",
        "test/5/5-0004.png",
        "test/5/5-0005.png",
        "test/5/5-0006.png",
        "test/5/5-0007.png",
    ]}
    second={[
        "test/5/5-0008.png",
        "test/5/5-0009.png",
        "test/5/5-0010.png",
        "test/5/5-0011.png",
        "test/5/5-0012.png",
        "test/5/5-0013.png",
        "test/5/5-0014.png",
        "test/5/5-0015.png",
    ]}
    third={[
        "test/5/5-0016.png",
        "test/5/5-0017.png",
        "test/5/5-0018.png",
        "test/5/5-0019.png",
        "test/5/5-0020.png",
        "test/5/5-0021.png",
        "test/5/5-0022.png",
        "test/5/5-0023.png",
    ]}
    fourth={[
        "test/5/5-0024.png",
        "test/5/5-0025.png",
        "test/5/5-0026.png",
        "test/5/5-0027.png",
        "test/5/5-0028.png",
        "test/5/5-0029.png",
        "test/5/5-0030.png",
        "test/5/5-0031.png",
    ]}
/>

### Sixes

<ImagesTable
    size={112}
    heading={"Sixes Images"}
    first={[
        "test/6/6-0000.png",
        "test/6/6-0001.png",
        "test/6/6-0002.png",
        "test/6/6-0003.png",
        "test/6/6-0004.png",
        "test/6/6-0005.png",
        "test/6/6-0006.png",
        "test/6/6-0007.png",
    ]}
    second={[
        "test/6/6-0008.png",
        "test/6/6-0009.png",
        "test/6/6-0010.png",
        "test/6/6-0011.png",
        "test/6/6-0012.png",
        "test/6/6-0013.png",
        "test/6/6-0014.png",
        "test/6/6-0015.png",
    ]}
    third={[
        "test/6/6-0016.png",
        "test/6/6-0017.png",
        "test/6/6-0018.png",
        "test/6/6-0019.png",
        "test/6/6-0020.png",
        "test/6/6-0021.png",
        "test/6/6-0022.png",
        "test/6/6-0023.png",
    ]}
    fourth={[
        "test/6/6-0024.png",
        "test/6/6-0025.png",
        "test/6/6-0026.png",
        "test/6/6-0027.png",
        "test/6/6-0028.png",
        "test/6/6-0029.png",
        "test/6/6-0030.png",
        "test/6/6-0031.png",
    ]}
/>

### Sevens

<ImagesTable
    size={112}
    heading={"Sevens Images"}
    first={[
        "test/7/7-0000.png",
        "test/7/7-0001.png",
        "test/7/7-0002.png",
        "test/7/7-0003.png",
        "test/7/7-0004.png",
        "test/7/7-0005.png",
        "test/7/7-0006.png",
        "test/7/7-0007.png",
    ]}
    second={[
        "test/7/7-0008.png",
        "test/7/7-0009.png",
        "test/7/7-0010.png",
        "test/7/7-0011.png",
        "test/7/7-0012.png",
        "test/7/7-0013.png",
        "test/7/7-0014.png",
        "test/7/7-0015.png",
    ]}
    third={[
        "test/7/7-0016.png",
        "test/7/7-0017.png",
        "test/7/7-0018.png",
        "test/7/7-0019.png",
        "test/7/7-0020.png",
        "test/7/7-0021.png",
        "test/7/7-0022.png",
        "test/7/7-0023.png",
    ]}
    fourth={[
        "test/7/7-0024.png",
        "test/7/7-0025.png",
        "test/7/7-0026.png",
        "test/7/7-0027.png",
        "test/7/7-0028.png",
        "test/7/7-0029.png",
        "test/7/7-0030.png",
        "test/7/7-0031.png",
    ]}
/>

### Eights

<ImagesTable
    size={112}
    heading={"Eights Images"}
    first={[
        "test/8/8-0000.png",
        "test/8/8-0001.png",
        "test/8/8-0002.png",
        "test/8/8-0003.png",
        "test/8/8-0004.png",
        "test/8/8-0005.png",
        "test/8/8-0006.png",
        "test/8/8-0007.png",
    ]}
    second={[
        "test/8/8-0008.png",
        "test/8/8-0009.png",
        "test/8/8-0010.png",
        "test/8/8-0011.png",
        "test/8/8-0012.png",
        "test/8/8-0013.png",
        "test/8/8-0014.png",
        "test/8/8-0015.png",
    ]}
    third={[
        "test/8/8-0016.png",
        "test/8/8-0017.png",
        "test/8/8-0018.png",
        "test/8/8-0019.png",
        "test/8/8-0020.png",
        "test/8/8-0021.png",
        "test/8/8-0022.png",
        "test/8/8-0023.png",
    ]}
    fourth={[
        "test/8/8-0024.png",
        "test/8/8-0025.png",
        "test/8/8-0026.png",
        "test/8/8-0027.png",
        "test/8/8-0028.png",
        "test/8/8-0029.png",
        "test/8/8-0030.png",
        "test/8/8-0031.png",
    ]}
/>

### Nines

<ImagesTable
    size={112}
    heading={"Nines Images"}
    first={[
        "test/9/9-0000.png",
        "test/9/9-0001.png",
        "test/9/9-0002.png",
        "test/9/9-0003.png",
        "test/9/9-0004.png",
        "test/9/9-0005.png",
        "test/9/9-0006.png",
        "test/9/9-0007.png",
    ]}
    second={[
        "test/9/9-0008.png",
        "test/9/9-0009.png",
        "test/9/9-0010.png",
        "test/9/9-0011.png",
        "test/9/9-0012.png",
        "test/9/9-0013.png",
        "test/9/9-0014.png",
        "test/9/9-0015.png",
    ]}
    third={[
        "test/9/9-0016.png",
        "test/9/9-0017.png",
        "test/9/9-0018.png",
        "test/9/9-0019.png",
        "test/9/9-0020.png",
        "test/9/9-0021.png",
        "test/9/9-0022.png",
        "test/9/9-0023.png",
    ]}
    fourth={[
        "test/9/9-0024.png",
        "test/9/9-0025.png",
        "test/9/9-0026.png",
        "test/9/9-0027.png",
        "test/9/9-0028.png",
        "test/9/9-0029.png",
        "test/9/9-0030.png",
        "test/9/9-0031.png",
    ]}
/>



<!--  -->

<ImagesTable
    size={112}
    heading={"Ones Images"}
    dirname={"train"}
    classname={"1"}
/>

<ImagesTable
    size={112}
    heading={"Ones Images"}
    dirname={"test"}
    classname={"9"}
/>