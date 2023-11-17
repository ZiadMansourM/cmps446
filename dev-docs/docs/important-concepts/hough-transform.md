---
sidebar_position: 1
id: Hough Transform
description: Visualization of Hough Transform
slug: /important-concepts/hough-transform
---

import UnderConstruction from "../../src/components/UnderConstruction.js";

# Hough Transform

## History
The Hough Transform is a feature extraction technique used in image analysis, computer vision, and digital image processing. The purpose of the technique is to find imperfect instances of objects within a certain class of shapes by a voting procedure. This voting procedure is carried out in a parameter space, from which object candidates are obtained as local maxima in an accumulator space. It was initially invented for machine analysis of bubble chamber photographs by Paul V.C. Hough in 1959 and patented in 1962 as "Method and Means for Recognizing Complex Patterns" - [Patent](https://patents.google.com/patent/US3069654)


## Hough Line
In the next video we have a 5*5 image with an edge at the diagonal. We will see how the Hough Transform works for this image. In both `Cartesian` and `Polar` Coordinates.

<div style={{ display: 'flex', justifyContent: 'center' }}>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/jOArJGp0twc?si=I09dI6PQH4vtyI7v" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

### Cartesian Coordinates
As you saw in the video above we had a 5*5 image with and edge at the diagonal. So while traversing image pixel by pixel once we reach an edge pixel:
- We Calculate its x and y coordinates.
```
- (0, 0)
- (1, 1)
- (2, 2)
- (3, 3)
- (4, 4)
```
- Say it was `(3, 3)`. We know from line equation that `y = mx + c`.
> We will use the plot on the right half of the video to visualize the possible outputs.
- For each value of `c` we will calculate the value of `m` and plot it on the graph. Using these equations: `m_value = lambda x, y, c: (y - c) / x`.
> Note that if `x==0` that would cause trouble.
- We then will use `c_value = lambda x, y, m: y - m * x` to calculate the value of `c` for each `m` and plot it on the graph.

```python
def get_two_points_on_line(i):
    """Returns two points on the line represented by the cell at index i
    Args:
        - i (int): index of the cell
    Returns:
        - first_point (tuple[float, float]): (x, y) coordinates of the first point
        - second_point (tuple[float, float]): (x, y) coordinates of the second point
    """
    x_value = lambda val: val // 5
    y_value = lambda val: val % 5
    if x_value(i) != 0:
        m_value = lambda x, y, c: (y - c) / x
        first_point = (-4, m_value(x_value(i), y_value(i), -4))
        second_point = (4, m_value(x_value(i), y_value(i), 4))
    else:
        c_value = lambda x, y, m: y - m * x
        first_point = (c_value(x_value(i), y_value(i), -4), -4)
        second_point = (c_value(x_value(i), y_value(i), 4), 4)
    return first_point, second_point
```


### Polar Coordinates
Due to undefined value of slope for vertical lines in cartesian coordinates, we have to move to polar coordinates. In polar coordinates line is define by ρ and θ where ρ is the norm distance of the line from origin. θ is the angle between the norm and the horizontal x axis. The equation of line in terms of ρ and θ now is`

![equation](https://latex.codecogs.com/svg.image?&space;y=\frac{-cos(\theta)}{sin(\theta)}x&plus;\frac{\rho}{sin(\theta)})

and

![equation](https://latex.codecogs.com/svg.image?\rho=x&space;cos(\theta)&plus;y&space;sin(\theta))


The Range of values of ρ and θ
- θ  in polar coordinate takes value in range of -90 to 90.
- The maximum norm distance is given by diagonal distance which is

![equation](https://latex.codecogs.com/svg.image?\rho_{max}=\sqrt{x^2&plus;y^2})

So ρ has values in range from `−ρmax` to `ρmax`.


## Hough Circle
<UnderConstruction />

## REFERENCES
- [Mansour, Z. (2023, November 17). Welcome to Visualizations Scripts of CMPS446. GitHub.](https://github.com/ZiadMansourM/manim)
- [Alaa, A. (n.d.). Week 4: Hough Transform (Line and Circle Detection). Tutorials for SBME Students.](https://sbme-tutorials.github.io/2021/cv/notes/4_week4.html)
- [Method and means for recognizing complex patterns. (n.d.).](https://patents.google.com/patent/US3069654)
- [Hough transform. (2020, April 12). Wikipedia.](https://en.wikipedia.org/wiki/Hough_transform)
