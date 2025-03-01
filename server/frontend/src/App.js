import LoginPanel from "./components/Login/Login"
import { Routes, Route } from "react-router-dom";
import React from 'react';
import { Routes, Route, BrowserRouter } from 'react-router-dom'; // Import react-router-dom components
import Home from './components/Home'; // Import the Home component
import About from './components/About'; // Import the About component
import Contact from './components/Contact'; // Import the Contact component
import Register from './components/Register/Register'; // Import the Register component
import Login from './components/Login/Login'; // Import the Login component

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} /> // Route for Home
        <Route path="/login" element={<Login />} /> // Route for Login
        <Route path="/register" element={<Register />} /> // Route for Registration
        <Route path="/about" element={<About />} /> // Route for About page
        <Route path="/contact" element={<Contact />} /> // Route for Contact page
        {/* Add additional routes as needed */}
      </Routes>
    </BrowserRouter>
  );
}

export default App;

