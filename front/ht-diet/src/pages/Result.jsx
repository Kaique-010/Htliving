import React, {useEffect, useState} from "react";
import {useLocation} from "react-router-dom";

const Result = () => {
  const location = useLocation();
  const [dataLoaded, setDataLoaded] = useState(false);
  const [resultText, setResultText] = useState("");

  useEffect(() => {
    if (location.state && location.state.data) {
      const data = location.state.data;
      const formattedText = formatText(data.text); // Formatar o texto aqui
      setResultText(formattedText);
      setDataLoaded(true);
    } else {
      console.log("Nenhum dado foi passado pela localização.");
      setDataLoaded(true);
    }
  }, [location]);

  // Função para formatar o texto com HTML
  const formatText = (text) => {
    return text
      .replace(/## (.+)/g, "<h2>$1</h2>") // Formatar cabeçalhos
      .replace(/\*\*(.+)\*\*/g, "<strong>$1</strong>") // Formatar negrito
      .replace(/\*(.+)\*/g, "<em>$1</em>") // Formatar itálico
      .replace(/\n/g, "<br/>"); // Quebra de linha
  };

  // Caso os dados ainda não estejam carregados
  if (!dataLoaded) {
    return <div>Carregando...</div>; // Indicador de carregamento
  }

  return (
    <div style={{padding: "20px", fontFamily: "Arial, sans-serif"}}>
      <h1 style={{textAlign: "center", color: "#4CAF50"}}>
        Resultado da Dieta Personalizada
      </h1>
      <h2 style={{textAlign: "center", color: "#8B8B8B"}}>
        Plano de Treino e Dieta Personalizada
      </h2>
      <div style={{marginBottom: "40px"}}>
        <h3>Plano Completo</h3>
        <div
          dangerouslySetInnerHTML={{__html: resultText}} 
        />
      </div>
    </div>
  );
};

export default Result;
