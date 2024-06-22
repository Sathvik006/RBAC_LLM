// src/components/QueryInput.js

import React from 'react';
import './QueryInput.css';
import { FaFileCsv } from 'react-icons/fa'; // Import CSV icon from react-icons/fa

function QueryInput({ query, setQuery, handleQuerySubmit, handleFileUpload }) {
  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleQuerySubmit();
    }
  };

  return (
    <div className="query-input-container">
      <div className="query-input">
        <input
          type="text"
          placeholder="Type your query here..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyPress={handleKeyPress}
        />
        <button className="send-button" onClick={handleQuerySubmit}>Send</button>
      </div>
      <button className="load-csv-button" onClick={handleFileUpload}>
        <FaFileCsv /> {/* Render CSV icon */}
      </button>
    </div>
  );
}

export default QueryInput;
