import React, { useState } from 'react';
import axios from 'axios';
import '../App.css'; // Updated custom CSS path

const CandidateRegister = () => {
  const [formData, setFormData] = useState({
    name: '',
    mobile: '',
    alternate_mobile: '',
    area: '',
    city: '',
    degree: '',
    department: '',
    passout_year: '',
    experience_years: '',
    experience_details: '',
    branch: '',
    resume: null,
    agreed_to_terms: false,
  });

  const [fileName, setFileName] = useState('');

  const handleChange = e => {
    const { name, value, type, checked, files } = e.target;
    if (type === 'file') {
      setFormData({ ...formData, resume: files[0] });
      setFileName(files[0]?.name || '');
    } else if (type === 'checkbox') {
      setFormData({ ...formData, [name]: checked });
    } else {
      setFormData({ ...formData, [name]: value });
    }
  };

  const handleSubmit = async e => {
    e.preventDefault();
    const data = new FormData();
    Object.entries(formData).forEach(([key, value]) => {
      data.append(key, value);
    });

    try {
      await axios.post('https://bluezapplication.onrender.com/api/candidates/', data, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      alert('✅ Candidate registered successfully!');
    } catch (error) {
      console.error('Error:', error.response?.data || error.message);
      alert('❌ Registration failed');
    }
  };

  return (
    <div className="register-container">
      <form className="register-form" onSubmit={handleSubmit}>
        <h2 className="form-title">Candidate Registration</h2>

        <input className="form-input" name="name" placeholder="Full Name" onChange={handleChange} required />
        <input className="form-input" name="mobile" placeholder="Mobile Number" onChange={handleChange} required />
        <input className="form-input" name="alternate_mobile" placeholder="Alternate Number" onChange={handleChange} />
        <input className="form-input" name="area" placeholder="Area" onChange={handleChange} required />
        <input className="form-input" name="city" placeholder="City" onChange={handleChange} required />
        <input className="form-input" name="degree" placeholder="Degree" onChange={handleChange} required />
        <input className="form-input" name="department" placeholder="Department" onChange={handleChange} required />
        <input className="form-input" type="number" name="passout_year" placeholder="Year of Passout" onChange={handleChange} required />
        <input className="form-input" type="number" name="experience_years" placeholder="Experience (Years)" onChange={handleChange} required />
        <textarea className="form-textarea" name="experience_details" placeholder="Experience Details" onChange={handleChange}></textarea>
        <input className="form-input" name="branch" placeholder="Branch" onChange={handleChange} required />

        <div className="form-group">
          <label className="form-label">Upload Resume (PDF only)</label>
          <input className="form-file" type="file" name="resume" accept=".pdf" onChange={handleChange} required />
          {fileName && (
            <div className="file-name">
              ✅ <strong>{fileName}</strong> selected
            </div>
          )}
        </div>

        <div className="form-check-group">
          <input className="form-check-input" type="checkbox" name="agreed_to_terms" onChange={handleChange} id="termsCheck" />
          <label className="form-check-label" htmlFor="termsCheck">
            I agree to all Terms
          </label>
        </div>

        <button className="submit-btn" type="submit">Register</button>
      </form>
    </div>
  );
};

export default CandidateRegister;
