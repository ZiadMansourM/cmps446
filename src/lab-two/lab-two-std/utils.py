import math
from typing import Union, Optional
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import skimage.io as io
from skimage.exposure import histogram
from matplotlib.pyplot import bar
from skimage.color import rgb2gray, rgb2hsv
from scipy.signal import convolve2d
from scipy import fftpack
from skimage.util import random_noise
from skimage.filters import median
from skimage.feature import canny
from skimage.filters import sobel_h, sobel, sobel_v, roberts, prewitt


def show_images(images: list[np.ndarray], titles: Optional[list[Union[str, None]]] = None) -> None:
    """Display a list of images with optional titles.

    Args:
        images (List[np.ndarray]): List of images to display.
        titles (Optional[List[Union[str, None]]]): List of titles for the images. If None, default titles will be used.

    Returns:
        None
    """
    n_ims = len(images)
    if titles is None:
        titles = [f'({i + 1})' for i in range(n_ims)]

    fig = plt.figure()
    for n, (image, title) in enumerate(zip(images, titles), start=1):
        a = fig.add_subplot(1, n_ims, n)
        if image.ndim == 2:
            plt.gray()
        plt.imshow(image)
        a.set_title(title)

    fig.set_size_inches(np.array(fig.get_size_inches()) * n_ims)
    plt.show()


def show_3d_image(img: np.ndarray, title: str) -> None:
    """
    Display a 3D surface plot of an image.

    Args:
        img (np.ndarray): The 3D image data.
        title (str): The title for the plot.

    Returns:
        None
    """
    fig = plt.figure()
    fig.set_size_inches((12,8))
    ax = fig.add_subplot(111, projection='3d')

    # Make data.
    X = np.arange(0, img.shape[0], 1)
    Y = np.arange(0, img.shape[1], 1)
    X, Y = np.meshgrid(X, Y)
    Z = img[X,Y]

    # Plot the surface.
    surf = ax.plot_surface(
        X, 
        Y, 
        Z, 
        cmap=cm.coolwarm, 
        linewidth=0, 
        antialiased=False
    )

    # Customize the z axis.
    ax.set_zlim(0, 8)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)
    ax.set_title(title)
    plt.show()


def show_3d_image_filtering_in_freq(img: np.ndarray, f: np.ndarray) -> None:
    """
    Display a 3D surface plot of image filtering in frequency domain.

    Args:
        img (np.ndarray): The original image data.
        f (np.ndarray): The filter in frequency domain.

    Returns:
        None
    """
    img_in_freq = fftpack.fft2(img)
    filter_in_freq = fftpack.fft2(f, img.shape)
    filtered_img_in_freq = np.multiply(img_in_freq, filter_in_freq)
    
    img_in_freq = fftpack.fftshift(np.log(np.abs(img_in_freq) + 1))
    filtered_img_in_freq = fftpack.fftshift(np.log(np.abs(filtered_img_in_freq) + 1))
    
    show_3d_image(img_in_freq, 'Original Image')
    show_3d_image(filtered_img_in_freq, 'Filtered Image')


def show_histogram(histogram_image: tuple) -> None:
    """
    Show a histogram for a grayscale image.

    Parameters:
        histogram_image (Tuple): A tuple containing histogram data.

    IMPORTANT Note:
        - The grayscale image should range from 0 to 1.
        - The histogram_image should contain histogram data in the format (values, bins).
    """
    plt.figure()
    bar(histogram_image[1] * 255, histogram_image[0], width=0.8, align='center')