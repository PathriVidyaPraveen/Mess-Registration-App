import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';  // Import your main component

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')  // This should match the div with id="root" in index.html
);
