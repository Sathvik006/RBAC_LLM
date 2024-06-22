// src/components/UserDropdown.js

import React, { useState } from 'react';
import { FaUser } from 'react-icons/fa'; // Importing Font Awesome user icon
import './UserDropdown.css';

const UserDropdown = ({ user, setUser }) => {
  const [isOpen, setIsOpen] = useState(false);
  const [searchTerm, setSearchTerm] = useState('');
  const userList = ['NIDeltaRole', 'DLDeltaRole']; // Example user list

  const toggleDropdown = () => {
    setIsOpen(!isOpen);
    setSearchTerm(''); // Clear search term on open
  };

  const handleUserSelect = (selectedUser) => {
    if (selectedUser === user) {
      setUser(null); // Deselect the user if it's already selected
    } else {
      setUser(selectedUser); // Select the new user
    }
    setIsOpen(false);
  };

  const handleSearchChange = (e) => {
    setSearchTerm(e.target.value);
  };

  const filteredUsers = userList.filter((user) =>
    user.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="user-dropdown">
      {!user ? (
        <button className="user-dropdown-button" onClick={toggleDropdown}>
          <FaUser className="user-icon" /> User
        </button>
      ) : (
        <button className="user-dropdown-button selected" onClick={toggleDropdown}>
          <FaUser className="user-icon" /> {user}
        </button>
      )}
      {isOpen && (
        <div className="user-dropdown-content">
          <input
            type="text"
            placeholder="Search users..."
            className="user-search-input"
            autoFocus // Focus the input field on dropdown open
            value={searchTerm}
            onChange={handleSearchChange}
          />
          {filteredUsers.map((userItem) => (
            <button
              key={userItem}
              className={user === userItem ? 'selected-user' : 'user-item'}
              onClick={() => handleUserSelect(userItem)}
            >
              {userItem}
            </button>
          ))}
        </div>
      )}
    </div>
  );
};

export default UserDropdown;
