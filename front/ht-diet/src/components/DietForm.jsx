import React, {useState} from "react";
import api from "../services/api";
import {useNavigate} from "react-router-dom";
import "./DietForm.css"; // Importando o CSS externo

const DietForm = ({onResult}) => {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    name: "",
    height: "",
    weight: "",
    train_freq: "",
    restrictions: "",
  });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false); // Estado para gerenciar o carregamento

  const handleChange = (e) => {
    const {name, value} = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    if (
      !formData.name ||
      !formData.height ||
      !formData.weight ||
      !formData.train_freq
    ) {
      setError("Preencha todos os campos obrigatórios!");
      return;
    }

    const prompt = `
      Crie uma dieta e um treino personalizados, para uma pessoa chamada ${
        formData.name
      }, que tem ${formData.height} cm de altura e pesa ${
      formData.weight
    } kg. Frequência de treino: ${formData.train_freq}. Restrições: ${
      formData.restrictions ? formData.restrictions : "Nenhuma"
    },
    { Sem recomendações, apenas o que é pedido e as observações de treino e dieta, não precisamos de dicas quanto a profissionais 
     de saúde ou educadores físicos
    }.
    
    `;

    const model = "gemini-1.5-flash";

    setLoading(true); // Ativar o estado de carregamento

    try {
      const response = await api.post("/gemini-prompt/", {prompt, model});

      if (response.status === 200 && response.data && response.data.text) {
        onResult(response.data);
        navigate("/result", {state: {data: response.data}});
      } else {
        setError("Erro ao processar a resposta da API.");
      }
    } catch (err) {
      setError("Erro ao enviar os dados. Verifique e tente novamente.");
    } finally {
      setLoading(false); // Desativar o estado de carregamento
    }
  };

  return (
    <div>
      {loading && (
        <div className="loading-overlay">
          <p>Carregando, por favor aguarde...</p>
        </div>
      )}
      <form onSubmit={handleSubmit} className="form-container">
        <input
          type="text"
          name="name"
          placeholder="Nome"
          value={formData.name}
          onChange={handleChange}
          required
        />
        <input
          type="number"
          name="height"
          placeholder="Altura (cm)"
          value={formData.height}
          onChange={handleChange}
          required
        />
        <input
          type="number"
          name="weight"
          placeholder="Peso (kg)"
          value={formData.weight}
          onChange={handleChange}
          required
        />
        <select
          name="train_freq"
          value={formData.train_freq}
          onChange={handleChange}
          required
        >
          <option value="">Selecione a frequência de treino</option>
          <option value="low">Baixa (1-2 vezes por semana)</option>
          <option value="medium">Média (3-4 vezes por semana)</option>
          <option value="high">Alta (5 ou mais vezes por semana)</option>
        </select>
        <input
          type="text"
          name="restrictions"
          placeholder="Restrições alimentares"
          value={formData.restrictions}
          onChange={handleChange}
        />
        <button type="submit" disabled={loading}>
          {loading ? "Enviando..." : "Enviar Dados"}
        </button>
        {error && <p className="error-message">{error}</p>}
      </form>
    </div>
  );
};

export default DietForm;
