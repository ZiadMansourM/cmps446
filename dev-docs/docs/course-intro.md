---
sidebar_position: 1
id: Introduction to CMPS446
description: 🚁 Helicopter view of Our Graduation Project.
slug: /
---

## Image Processing is Different
First, we would like to welcome you to CMPS446 `Image Processing and Computer Vision` course. We hope that you will enjoy the course and adds to your knowledge and experience.

Please, make your priority to `understand`, `discuss` and to ask freely ... remember grades are not the goal, but the knowledge and experience you gain is.


## Course System
- Official Site: [elearn.eng.cu.edu.eg](http://www.elearn.eng.cu.edu.eg/)
- Enroll yourself in the corresponding group "Credit/Mainstream".
- Quiz during the first 5 minutes of each tutorial.

## Tools
- [Python](https://www.python.org/).
- Packages: "NumPy, SciPy, Matplotlib, OpenCV, ...".
- IDE: "Anaconda, Jupiter Notebooks, VSCode, ...".
- Keep outputs and variables in memory till discussions.

## Course Overview
- Introduction to computer vision.
- Image and Camera Fundamentals.
- Basic concepts of DIP (Fourier Transform & Convolution).
- Image preprocessing techniques "e.g. Contrast enhancement".
- Morphological image processing techniques.
- Image segmentation techniques.
- Image Feature Extraction "e.g. Edge detection, SIFT, Textures, Corner Detection, ...".
- Pattern Recognition and Classification.
- Computer Vision Applications.


export const CenterContainer = ({ children }) => (
  <div style={{ textAlign: 'center' }}>
    {children}
  </div>
);

export const Table = ({ headers, rows }) => (
  <div style={{ display: 'inline-block' }}>
    <table>
      <tbody>
        <tr>
          <td colSpan={3} style={{ textAlign: 'center' }}>TAs Team</td>
        </tr>
        <tr>
          {headers.map(header => <th key={header}>{header}</th>)}
        </tr>
        {rows.map((row, rowIndex) => (
          <tr key={rowIndex}>
            {Array.isArray(row) ? row.map((cell, cellIndex) => <td key={cellIndex}>{cell}</td>) : null}
          </tr>
        ))}
      </tbody>
    </table>
  </div>
);

<CenterContainer>
  <Table
    headers={['Name', 'Email', 'Telephone']}
    rows={[
      ['Mohamed Shawky', '-', '-'],
      ['Remonda Talaat', '-', '-'],
      ['Habiba Assem', '-', '-'],
      ['Ziad Mansour', 'ziadmansour.4.9.2000@gmail.com', <a href="https://wa.me/201021799950">+201021799950</a>],
      ['Hussien Mostafa', '-', '-'],
    ]}
  />
</CenterContainer>

## 🏛️ Datasets

| Status | Dataset Link | Description |
|--------|--------------|-------------|
| ❌  | [Gingerbread Man](https://www.capturingreality.com/free-datasets) | 3D model of a gingerbread cookie. Created in RealityCapture from 158 images. |
| ❌  | [Hammer](https://www.capturingreality.com/free-datasets) | Hammer dataset with size of 750 MB. |
| ❌  | [Small Cottage](https://www.capturingreality.com/free-datasets) | Objects Scanned from all sides using Masks. |
| ❌  | [Fountain](https://sketchfab.com/3d-models/fountain-dataset-bdcf73513f404370a80cd3d8d0871fa8) | 3D reconstruction images from the popular Strecha dataset. |


## ⚖️ License

This project is licensed under the terms of the GNU General Public License version 3.0 (GPLv3). See the LICENSE file for details.


[docs]: https://docs.scanmate.sreboy.com/
[videos]: https://www.youtube.com/playlist?list=PLtRAgw3FCYeBXUeBIDOmbzzEEryIvtJo3