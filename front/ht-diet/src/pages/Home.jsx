import React, { useState } from "react";
import DietForm from "../components/DietForm";
import DietResult from "../components/DietResult";

// Importando o ícone do FontAwesome
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faDumbbell } from "@fortawesome/free-solid-svg-icons";  // Ícone do haltere
import { faHeart } from "@fortawesome/free-regular-svg-icons";   // Ícone do coração

const Home = () => {
  const [result, setResult] = useState(null);

  return (
    <div className="container"> {/* Alterei container para className */}
      <h2>
        Plano de Dieta e Treinos
        {/* Ícones abaixo do texto */}
        <div className="icon-container">
          <FontAwesomeIcon icon={faDumbbell} />
          <FontAwesomeIcon icon={faHeart} />
        </div>
      </h2>
      <DietForm onResult={setResult} />
      {result && <DietResult data={result} />}
    </div>
  );
};

export default Home;
