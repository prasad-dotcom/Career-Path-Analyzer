import React from "react";
import { createRoot } from "react-dom/client";
import App from "./App";
import "./styles.css";

function initializeApp() {
  const container = document.getElementById("root");
  if (container) {
    const root = createRoot(container);
    root.render(<App />);
  } else {
    console.error("Root element not found");
  }
}

// Wait for DOM to be ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initializeApp);
} else {
  // DOM is already loaded
  initializeApp();
}
