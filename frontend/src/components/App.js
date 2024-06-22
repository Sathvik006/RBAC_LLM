// src/components/App.js

import React, { useState } from 'react';
import './App.css';
import UserDropdown from './UserDropdown';
import QueryInput from './QueryInput';
import ResponseDisplay from './ResponseDisplay';

function App() {
  const [user, setUser] = useState(null); // Initially no user is selected
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');
  const [statusMessage, setStatusMessage] = useState('');

  const handleQuerySubmit = async () => {
    const response = await fetch('http://localhost:5000/query', { // Modify endpoint to localhost:5000
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ user, query }), // Include user in the request body
    });

    const data = await response.json();
    setResponse(data.answer);
  };

  const handleFileUpload = async () => {
    const fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.accept = '.csv';
    fileInput.onchange = async (e) => {
      const file = e.target.files[0];
      const formData = new FormData();
      formData.append('file', file);

      try {
        const response = await fetch('http://localhost:5000/upload', { // Modify endpoint to localhost:5000
          method: 'POST',
          body: formData,
        });

        if (!response.ok) {
          throw new Error('Failed to upload file');
        }

        const result = await response.json();
        setStatusMessage(result.message);
      } catch (error) {
        setStatusMessage(`Error uploading file: ${error.message}`);
      }
    };

    fileInput.click(); // Trigger file input dialog
  };

  return (
    <div className="App">
      <header className="header">
        <UserDropdown user={user} setUser={setUser} />
      </header>
      <div className="main-content">
        <ResponseDisplay response={response} />
        <div className="query-container">
          <QueryInput query={query} setQuery={setQuery} handleQuerySubmit={handleQuerySubmit} handleFileUpload={handleFileUpload} />
        </div>
        {statusMessage && <p className="status-message">{statusMessage}</p>}
      </div>
    </div>
  );
}

export default App;
