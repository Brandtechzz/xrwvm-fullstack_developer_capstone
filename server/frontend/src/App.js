import React from "react";
import { Routes, Route } from "react-router-dom";
import LoginPanel from "./components/Login/Login"; // Assuming you have a Login component
import Register from "./components/Register/Register";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      <Route path="/register" element={<Register />} /> // Route for registration
    </Routes>
  );
}
export default App;
