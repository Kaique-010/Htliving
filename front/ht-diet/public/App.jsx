import React from "react";
import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import Home from "./pages/Home";
import DietForm from "./components/DietForm";
import Result from "./pages/Result"; // Adicione a página de resultado

const App = () => (
  <Router>
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/diet-form" element={<DietForm />} />
      <Route path="/result" element={<Result />} />{" "}
      {/* Rota para a página de resultado */}
    </Routes>
  </Router>
);

export default App;
