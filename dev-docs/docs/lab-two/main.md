---
sidebar_position: 1
id: Concepts Review
description: Quick Review of Concepts.
slug: /lab-two/basic-concepts
---

## Histogram Equalization

### Sample Code
```python
from collections import Counter
from pathlib import Path
from typing import Final

import cv2
import matplotlib.pyplot as plt
import numpy as np


def __show_image(window_name: str, image: np.ndarray) -> None:
    cv2.startWindowThread()
    cv2.imshow(window_name, image)
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyWindow(window_name)
    for _ in range(5):
        cv2.waitKey(1)


def show_images(images, titles=None):
    num_images = len(images)

    num_rows = 1
    num_cols = num_images

    if titles is None:
        titles = [f'Image {i}' for i in range(1, num_images + 1)]

    plt.figure(figsize=(15, 5))

    for i, (image, title) in enumerate(zip(images, titles), 1):
        plt.subplot(num_rows, num_cols, i)
        plt.imshow(image, cmap='gray')
        plt.title(title)
        plt.axis('off')

    plt.show()


BASE_DIR: Final[Path] = Path().resolve()
DATA_DIR: Final[Path] = os.path.join(BASE_DIR, 'data')

# Load an image
image = cv2.imread(os.path.join(DATA_DIR, 'example-one', 'low-contrast.png'))

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Perform histogram equalization
equalized_image = cv2.equalizeHist(gray_image)

# Calculate the histogram of the original image using Counter
original_histogram = Counter(gray_image.flatten())

# Calculate the histogram of the equalized image using Counter
equalized_histogram = Counter(equalized_image.flatten())

# Display the original and equalized images
__show_image("Original Gray Image", gray_image)
__show_image("Equalized Image", equalized_image)

cv2.imwrite(os.path.join(DATA_DIR, 'example-one', 'equalized.png'), equalized_image)

show_images([gray_image, equalized_image], ['Original Image', 'Equalized Image'])

# Plot the original histogram
plt.figure(figsize=(8, 6))
plt.subplot(2, 2, 3)
intensities_original = sorted(original_histogram.keys())
counts_original = [original_histogram[intensity] for intensity in intensities_original]
plt.bar(intensities_original, counts_original, width=1.0, color='b', alpha=0.7)
plt.title('Original Histogram')
plt.xlabel('Intensity')
plt.ylabel('Count')

# Plot the equalized histogram
plt.subplot(2, 2, 4)
intensities_equalized = sorted(equalized_histogram.keys())
counts_equalized = [equalized_histogram[intensity] for intensity in intensities_equalized]
plt.bar(intensities_equalized, counts_equalized, width=1.0, color='g', alpha=0.7)
plt.title('Equalized Histogram')
plt.xlabel('Intensity')
plt.ylabel('Count')

plt.tight_layout()
plt.show()
```

<hr/>

### Example One
Orginal Image | Equalized Image
:--:|:--:
![original](/assets/histogram-equalization/example-one/low-contrast.png) | ![equalized](/assets/histogram-equalization/example-one/equalized.png)

![histogram](/assets/histogram-equalization/example-one/histograms.png)

<hr/>

### Example Two
Orginal Image | Equalized Image
:--:|:--:
![original](/assets/histogram-equalization/example-two/low-contrast.png) | ![equalized](/assets/histogram-equalization/example-two/equalized.png)

![histogram](/assets/histogram-equalization/example-two/histograms.png)

<hr/>

### Example Three
Orginal Image | Equalized Image
:--:|:--:
![original](/assets/histogram-equalization/example-three/low-contrast.png) | ![equalized](/assets/histogram-equalization/example-three/equalized.png)

![histogram](/assets/histogram-equalization/example-three/histograms.png)

<hr/>

### Example Four
Orginal Image | Equalized Image
:--:|:--:
![original](/assets/histogram-equalization/example-four/low-contrast.png) | ![equalized](/assets/histogram-equalization/example-four/equalized.png)

![histogram](/assets/histogram-equalization/example-four/histograms.png)