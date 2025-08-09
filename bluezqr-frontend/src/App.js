import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import CandidateRegister from "./components/CandidateRegister";
import StudentRegister from "./components/StudentRegister";
import Home from "./components/Home";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/candidate-register" element={<CandidateRegister />} />
        <Route path="/student-register" element={<StudentRegister />} />
      </Routes>
    </Router>
  );
}

export default App;
