---
sidebar_position: 4
id: Lab Requirements
description: Explanation of lab requirements.
slug: /lab-one/lab-requirements
---

## 📝 Lab Requirements
- [ ] HSV.
- [ ] Histograms.
- [ ] Noise.

## Prerequisites

### Images Types

True Color | Gray Scale | Binary
:---: | :---: | :---: |
![Original](/assets/images-types/original.png) | ![Gray](/assets/images-types/gray.png) | ![Mask](/assets/images-types/mask.png)

<hr/>

Original Image | Gray
:---: | :---:
![Original](/assets/images-types/original.png) | ![Gray](/assets/images-types/gray.png)


Original Image | Mask
:---: | :---:
![Original](/assets/images-types/original.png) | ![Mask](/assets/images-types/mask.png)

Original Image | XORed
:---: | :---:
![Original](/assets/images-types/original.png) | ![XORed](/assets/images-types/xored.png)

Original Image | SIFT
:---: | :---:
![Original](/assets/images-types/sift_without_mask.png) | ![SIFT](/assets/images-types/sift.png)

### NumPy Arrays
Numpy is a great mathematical library that deals with array. To construct array of zeros [5,5,5] all of unit8 (range from 0 to 255):
```python
(.venv) ziadh@Ziads-MacBook-Air cmps446 % python3 
Python 3.11.5 (v3.11.5:cce6ba91b3, Aug 24 2023, 10:50:31) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy as np
>>> array: np.ndarray = np.zeros(shape=(3, 5, 5), dtype=np.uint8)
>>> array
array([[[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]],

       [[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]],

       [[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]]], dtype=uint8)
>>> array[:,1:4,1:4] = 20
>>> array[:,:,:]
array([[[ 0,  0,  0,  0,  0],
        [ 0, 20, 20, 20,  0],
        [ 0, 20, 20, 20,  0],
        [ 0, 20, 20, 20,  0],
        [ 0,  0,  0,  0,  0]],

       [[ 0,  0,  0,  0,  0],
        [ 0, 20, 20, 20,  0],
        [ 0, 20, 20, 20,  0],
        [ 0, 20, 20, 20,  0],
        [ 0,  0,  0,  0,  0]],

       [[ 0,  0,  0,  0,  0],
        [ 0, 20, 20, 20,  0],
        [ 0, 20, 20, 20,  0],
        [ 0, 20, 20, 20,  0],
        [ 0,  0,  0,  0,  0]]], dtype=uint8)
>>> copied_array: np.ndarray = np.copy(array)
>>> copied_array
array([[[ 0,  0,  0,  0,  0],
        [ 0, 20, 20, 20,  0],
        [ 0, 20, 20, 20,  0],
        [ 0, 20, 20, 20,  0],
        [ 0,  0,  0,  0,  0]],

       [[ 0,  0,  0,  0,  0],
        [ 0, 20, 20, 20,  0],
        [ 0, 20, 20, 20,  0],
        [ 0, 20, 20, 20,  0],
        [ 0,  0,  0,  0,  0]],

       [[ 0,  0,  0,  0,  0],
        [ 0, 20, 20, 20,  0],
        [ 0, 20, 20, 20,  0],
        [ 0, 20, 20, 20,  0],
        [ 0,  0,  0,  0,  0]]], dtype=uint8)
>>> copied_array[:,1:3,1:3] = 70
>>> copied_array
array([[[ 0,  0,  0,  0,  0],
        [ 0, 70, 70, 20,  0],
        [ 0, 70, 70, 20,  0],
        [ 0, 20, 20, 20,  0],
        [ 0,  0,  0,  0,  0]],

       [[ 0,  0,  0,  0,  0],
        [ 0, 70, 70, 20,  0],
        [ 0, 70, 70, 20,  0],
        [ 0, 20, 20, 20,  0],
        [ 0,  0,  0,  0,  0]],

       [[ 0,  0,  0,  0,  0],
        [ 0, 70, 70, 20,  0],
        [ 0, 70, 70, 20,  0],
        [ 0, 20, 20, 20,  0],
        [ 0,  0,  0,  0,  0]]], dtype=uint8)
>>> array[:,:,:]
array([[[ 0,  0,  0,  0,  0],
        [ 0, 20, 20, 20,  0],
        [ 0, 20, 20, 20,  0],
        [ 0, 20, 20, 20,  0],
        [ 0,  0,  0,  0,  0]],

       [[ 0,  0,  0,  0,  0],
        [ 0, 20, 20, 20,  0],
        [ 0, 20, 20, 20,  0],
        [ 0, 20, 20, 20,  0],
        [ 0,  0,  0,  0,  0]],

       [[ 0,  0,  0,  0,  0],
        [ 0, 20, 20, 20,  0],
        [ 0, 20, 20, 20,  0],
        [ 0, 20, 20, 20,  0],
        [ 0,  0,  0,  0,  0]]], dtype=uint8)
>>> copied_array[:,1:3,1:3] = 255
>>> copied_array[:,1:3,1:3] = 256
<stdin>:1: DeprecationWarning: NumPy will stop allowing conversion of out-of-bound Python integers to integer arrays.  The conversion of 256 to uint8 will fail in the future.
For the old behavior, usually:
    np.array(value).astype(dtype)
will give the desired result (the cast overflows).
>>> copied_array[:,1:3,1:3] = 700
<stdin>:1: DeprecationWarning: NumPy will stop allowing conversion of out-of-bound Python integers to integer arrays.  The conversion of 700 to uint8 will fail in the future.
For the old behavior, usually:
    np.array(value).astype(dtype)
will give the desired result (the cast overflows).
>>> 
```

### Reading and Showing Images
```python
import skimage.io as io

img = io.imread(‘image.png’)
io.show()
```

### Normalize unit8 images
```python
import numpy as np

# Create a sample uint8 image
uint8_image = np.array([
    [100, 200, 50],
    [25, 150, 75],
    [0, 255, 30]
], dtype=np.uint8)

# Normalize the uint8 image to the range [0, 1]
normalized_image = uint8_image / uint8_image.max()

print(normalized_image)
```

```console
[[0.39215686 0.78431373 0.19607843]
 [0.09803922 0.58823529 0.29411765]
 [0.         1.         0.11764706]]
```

## REFERENCES
- [Filters References](https://scikit-image.org/docs/dev/api/skimage.filters.html)
- [ImNoise](http://scikit-image.org/docs/dev/api/skimage.util.html)
- [Features (including Canny)](http://scikit-image.org/docs/dev/api/skimage.feature.html)
- [Equalize_hist](http://scikit-image.org/docs/dev/api/skimage.exposure.html#skimage.exposure.equalize_hist)