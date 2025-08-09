import React, { useState } from 'react';
import axios from 'axios';
import '../App.css'; // Custom CSS file

const StudentRegister = () => {
  const [formData, setFormData] = useState({
    name: '', mobile: '', alternate_mobile: '', degree: '', department: '',
    college_name: '', area: '', city: '', passout_year: '', percentage: '', resume: null
  });

  const [fileName, setFileName] = useState('');

  const handleChange = e => {
    const { name, value, files } = e.target;
    if (name === 'resume') {
      setFormData({ ...formData, resume: files[0] });
      setFileName(files[0]?.name || '');
    } else {
      setFormData({ ...formData, [name]: value });
    }
  };

  const handleSubmit = async e => {
    e.preventDefault();
    const data = new FormData();
    Object.entries(formData).forEach(([key, value]) => data.append(key, value));

    try {
      await axios.post('https://bluezapplication.onrender.com/api/students/', data, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
      alert("✅ Registered Successfully");
    } catch (err) {
      console.error(err);
      alert("❌ Registration Failed");
    }
  };

  return (
    <div className="student-form-container">
      <form className="student-form" onSubmit={handleSubmit}>
        <h2 className="form-title">Student Registration</h2>

        <input className="form-input" name="name" onChange={handleChange} placeholder="Name" required />
        <input className="form-input" name="mobile" onChange={handleChange} placeholder="Mobile" required />
        <input className="form-input" name="alternate_mobile" onChange={handleChange} placeholder="Alternate Mobile" />
        <input className="form-input" name="degree" onChange={handleChange} placeholder="Degree" required />
        <input className="form-input" name="department" onChange={handleChange} placeholder="Department" required />
        <input className="form-input" name="college_name" onChange={handleChange} placeholder="College Name" required />
        <input className="form-input" name="area" onChange={handleChange} placeholder="Area" required />
        <input className="form-input" name="city" onChange={handleChange} placeholder="City" required />
        <input className="form-input" name="passout_year" onChange={handleChange} placeholder="Year of Passout" required />
        <input className="form-input" name="percentage" onChange={handleChange} placeholder="Percentage" required />

        <div className="form-group">
          <label className="form-label">Upload Resume (PDF only)</label>
          <input
            className="form-file"
            type="file"
            name="resume"
            accept=".pdf"
            onChange={handleChange}
            required
          />
          {fileName && <p className="file-name">✅ {fileName}</p>}
        </div>

        <button className="submit-btn" type="submit">Register</button>
      </form>
    </div>
  );
};

export default StudentRegister;
