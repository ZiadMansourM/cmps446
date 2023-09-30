---
sidebar_position: 3
id: HSV Color Model
description: Deep dive into HSV Color Model.
slug: /lab-one/hsv
---

## Pixels

<div style={{ display: 'flex', justifyContent: 'center' }}>
  <iframe
    width="560"
    height="315"
    src="https://www.youtube.com/embed/zzF1O9rKcvY"
    frameborder="0"
    allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen
  ></iframe>
</div>

## HSV Color Space

![hsvcone](/assets/hsv/hsv.png)

The HSV color space (hue, saturation, value) is often used by people who are selecting colors (e.g., of paints or inks) from a color wheel or palette, because it corresponds better to how people experience color than the RGB color space does.

### Hue
Hues are the three primary colors (red, blue, and yellow) and the three secondary colors (orange, green, and violet) that appear in the color wheel or color circle. When you refer to hue, you are referring to pure color, or the visible spectrum of basic colors that can be seen in a rainbow. Colors vary from red, through yellow, green, cyan, blue, and magenta, back to red, so that there are actually red values both at 0 and 360.

### Saturation
Color saturation is the purity and intensity of a color as displayed in an image. The higher the saturation of a color, the more vivid and intense it is. The lower a color’s saturation, or chroma, the closer it is to pure gray on the grayscale.

### Value
Color value refers to the relative lightness or darkness of a color. We perceive color value based on the quantity of light reflected off of a surface and absorbed by the human eye. We refer to the intensity of the light that reaches the eye as “luminance.”

## Example
To better understand the HSV color space, we will use the following image:

```Matlab
% This is matlab code
first=1024;
second=first*3;

RGB=reshape(ones(first,1)*reshape(jet(first),1,second),[first,first,3]);
HSV=rgb2hsv(RGB);
H=HSV(:,:,1);
S=HSV(:,:,2);
V=HSV(:,:,3);
imshow(H)
figure, imshow(S);
figure, imshow(V);
figure, imshow(RGB);
R=RGB(:,:,1);
G=RGB(:,:,2);
B=RGB(:,:,3);
figure, imshow(R);
figure, imshow(G);
figure, imshow(B);
```

Orginal Image | Hue Plain | Saturation Plain | Value Plain
:--:|:--:|:--:|:--:
![original](/assets/hsv/rainbow.png) | ![hue](/assets/hsv/hue.png) | ![saturation](/assets/hsv/saturation.png) | ![value](/assets/hsv/value.png)

Orginal Image | Red Plain | Green Plain | Blue Plain
:--:|:--:|:--:|:--:
![original](/assets/hsv/rainbow.png) | ![red](/assets/hsv/r.png) | ![green](/assets/hsv/g.png) | ![blue](/assets/hsv/b.png)


### Explanation HSV Space

Orginal Image | Hue Plain
:--:|:--:
![original](/assets/hsv/rainbow.png) | ![hue](/assets/hsv/hue.png)

As you can see by looking at the hue plane image, hue values make a nice linear transition from high to low. If you compare the hue plane image against the original image, you can see that shades of deep blue have the highest values, and shades of deep red have the lowest values. 
(In Reality, there are values of red on both ends of the hue scale. To avoid confusion, our sample image uses only the red values from the beginning of the hue range.)

<hr/>

Orginal Image | Saturation Plain
:--:|:--:
![original](/assets/hsv/rainbow.png) | ![saturation](/assets/hsv/saturation.png)

Saturation can be thought of as the purity of a color. As the saturation plane image shows, the colors with the highest saturation have the highest values and are represented as white. In the center of the saturation image, notice the various shades of gray. These correspond to a mixture of colors; the cyans, greens, and yellow shades are mixtures of true colors.

<hr/>

Orginal Image | Value Plain
:--:|:--:
![original](/assets/hsv/rainbow.png) | ![value](/assets/hsv/value.png)

Value is roughly equivalent to brightness, and you will notice that the brightest areas of the value plane correspond to the brightest colors in the original image.

### Explanation RGB Space

Orginal Image | Red Plain
:--:|:--:
![original](/assets/hsv/rainbow.png) | ![red](/assets/hsv/r.png)

<hr/>

Orginal Image | Green Plain
:--:|:--:
![original](/assets/hsv/rainbow.png) | ![green](/assets/hsv/g.png)

<hr/>

Orginal Image | Blue Plain
:--:|:--:
![original](/assets/hsv/rainbow.png) | ![blue](/assets/hsv/b.png)

## REFERENCES
- [How to Use HSV Color Model in Photography - Master Class](https://en.wikipedia.org/wiki/HSL_and_HSV)
- [HSV Color Space - Image Processing Toolbox](http://www.ece.northwestern.edu/local-apps/matlabhelp/toolbox/images/color11.html)