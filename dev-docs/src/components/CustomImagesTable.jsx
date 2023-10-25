import React from 'react';

const CustomImagesTable = ({ dirname, classdigit, heading, size, imagePaths }) => {
  const chunkedElements = [];

  // Chunk the imagePaths array into groups of 8
  for (let i = 0; i < imagePaths.length; i += 8) {
    const rowImages = imagePaths.slice(i, i + 8);
    chunkedElements.push(rowImages);
  }

  return (
    <div style={{ display: 'inline-block' }}>
      <table>
        <tbody>
          <tr>
            <td colSpan={8} style={{ textAlign: 'center' }}>
              {heading}
            </td>
          </tr>
          {chunkedElements.map((row, rowIndex) => (
            <tr key={rowIndex}>
              {row.map((imagePath, index) => {
                // Extract the wrong predicted label from the image path
                const imageName = imagePath.split('/').pop();
                const wrongLabel = imageName.split('-')[2].split('.')[0];
                return (
                  <td key={index}>
                    <p style={{ textAlign: 'center' }}>{wrongLabel}</p>
                    <img
                      src={`/assets/datasets/minst/${dirname}/${classdigit}/${imagePath}`}
                      width={size}
                      height={size}
                    />
                  </td>
                );
              })}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default CustomImagesTable;
