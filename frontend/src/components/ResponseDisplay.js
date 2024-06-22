// src/components/ResponseDisplay.js

import React from 'react';
import './ResponseDisplay.css';

function ResponseDisplay({ response }) {
  return (
    <div className="response-display">
      <div className="message received">
        <div className="message-content">
          <p>{response}</p>
        </div>
      </div>
    </div>
  );
}

export default ResponseDisplay;
