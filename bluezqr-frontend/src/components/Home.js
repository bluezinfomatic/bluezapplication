import React from "react";
import { QRCodeCanvas } from "qrcode.react";
import "../App.css"; // Custom styles

const Home = () => {
  const baseURL = "https://bluezapplication.netlify.app"; // Replace with your live frontend URL
  const candidateURL = `${baseURL}/candidate-register`;
  const studentURL = `${baseURL}/student-register`;


  return (
    <>
     <div className="home-container">
      <div className="company-section">
        <h2>WELCOME TO DREAM FACTORY</h2>
        <p>
          <strong>Bluez Infomatic</strong> is sprouted as one of the leading BPO in providing highly
          challenged technical solutions for complex businesses. Bluez Infomatic Solutions have been
          empowering clients around the world to achieve business transformation and growth through
          its services that boost process and operational efficiencies. We offer seamless and the
          most affordable BPO and KPO solutions.
        </p>
        <p>
          We have expertise in every business and knowledge process like Data Administration,
          Inbound-outbound call services, Telemarketing services, Online Data Entry, Data Conversion
          Process, Data Backups, Web Development, Web Hosting and Maintenance Services along with
          SEO for effective Internet Marketing. Our operations are based in India to provide
          cost-effective services to our clients, with expansion of more BPO units underway.
        </p>
      </div>

      <div className="qr-wrapper">
        <div className="qr-box">
          <h3>Scan to Candidate Register</h3>
          <QRCodeCanvas value={candidateURL} size={160} />
        </div>
        <div className="qr-box">
          <h3>Scan to Student Register</h3>
          <QRCodeCanvas value={studentURL} size={160} />
        </div>
      </div>

      
    </div>
    </>
  );
};

export default Home;
