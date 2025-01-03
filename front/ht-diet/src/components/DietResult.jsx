import React from "react";

const DietResult = ({data}) => {
  if (!data) return <p>Carregando...</p>;

  return (
    <div>
      <h2>Resultado</h2>
      <p>{data.diet || data.train}</p>
    </div>
  );
};

export default DietResult;
