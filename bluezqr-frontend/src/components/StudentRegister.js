import React, { useState } from 'react';
import axios from 'axios';
import '../App.css'; // Your custom CSS

const StudentRegister = () => {
  const [formData, setFormData] = useState({
    name: '',
    mobile: '',
    alternate_mobile: '',
    degree: '',
    department: '',
    college_name: '',
    area: '',
    city: '',
    passout_year: '',
    percentage: '',
    resume: null
  });

  const [fileName, setFileName] = useState('');

  // Handle input change
  const handleChange = e => {
    const { name, value, files } = e.target;
    if (name === 'resume') {
      setFormData({ ...formData, resume: files[0] });
      setFileName(files[0]?.name || '');
    } else {
      setFormData({ ...formData, [name]: value });
    }
  };

  // Handle form submit
  const handleSubmit = async e => {
    e.preventDefault();

    const data = new FormData();
    data.append('name', formData.name);
    data.append('mobile', formData.mobile);
    data.append('alternate_mobile', formData.alternate_mobile || '');
    data.append('degree', formData.degree);
    data.append('department', formData.department);
    data.append('college_name', formData.college_name);
    data.append('area', formData.area);
    data.append('city', formData.city);
    data.append('passout_year', parseInt(formData.passout_year));
    data.append('percentage', parseFloat(formData.percentage));
    if (formData.resume) data.append('resume', formData.resume);

    try {
      const response = await axios.post(
        'https://bluezapplication.onrender.com/api/students/',
        data,
        { headers: { 'Content-Type': 'multipart/form-data' } }
      );
      console.log('Response:', response.data);
      alert('✅ Registered Successfully');
      setFormData({
        name: '',
        mobile: '',
        alternate_mobile: '',
        degree: '',
        department: '',
        college_name: '',
        area: '',
        city: '',
        passout_year: '',
        percentage: '',
        resume: null
      });
      setFileName('');
    } catch (err) {
      console.error('Error:', err.response?.data || err);
      alert('❌ Registration Failed');
    }
  };

  return (
    <div className="student-form-container">
      <form className="student-form" onSubmit={handleSubmit}>
        <h2 className="form-title">Student Registration</h2>

        <input className="form-input" name="name" value={formData.name} onChange={handleChange} placeholder="Name" required />
        <input className="form-input" name="mobile" value={formData.mobile} onChange={handleChange} placeholder="Mobile" required />
        <input className="form-input" name="alternate_mobile" value={formData.alternate_mobile} onChange={handleChange} placeholder="Alternate Mobile" />
        <input className="form-input" name="degree" value={formData.degree} onChange={handleChange} placeholder="Degree" required />
        <input className="form-input" name="department" value={formData.department} onChange={handleChange} placeholder="Department" required />
        <input className="form-input" name="college_name" value={formData.college_name} onChange={handleChange} placeholder="College Name" required />
        <input className="form-input" name="area" value={formData.area} onChange={handleChange} placeholder="Area" required />
        <input className="form-input" name="city" value={formData.city} onChange={handleChange} placeholder="City" required />
        <input className="form-input" name="passout_year" value={formData.passout_year} onChange={handleChange} placeholder="Year of Passout" required />
        <input className="form-input" name="percentage" value={formData.percentage} onChange={handleChange} placeholder="Percentage" required />

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
