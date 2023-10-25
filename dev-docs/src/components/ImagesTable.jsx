import React from 'react';

const ImagesTable = ({ dirname, classdigit, heading, size }) => {
  // Create an array to store the JSX elements
  const imageElements = [];

  for (let i = 0; i < 32; i++) {
    imageElements.push(
      <td key={i}>
        <img
          src={`/assets/datasets/minst/${dirname}/${classdigit}/${classdigit}-${i.toString().padStart(4, '0')}.png`}
          width={size}
          height={size}
        />
      </td>
    );
  }

  // Chunk the elements into rows with 8 items each
  const chunkedElements = [];
  for (let i = 0; i < imageElements.length; i += 8) {
    chunkedElements.push(imageElements.slice(i, i + 8));
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
              {row}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ImagesTable;
