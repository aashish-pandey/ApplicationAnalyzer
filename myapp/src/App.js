import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import UniversityPredict from './components/UniversityPredict';
import PredictionCalculatorForm from './components/PredictionCalculatorForm';
import UniversityPredictions from './components/UniversityPredictions';

function App() {
  return (

    
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={ <PredictionCalculatorForm/> } />
          <Route path="/uniPredictions" element={ <UniversityPredictions/> } />
          <Route path="/predictions" element={ <UniversityPredict uniname="UCLA" prediction="97"/> } />
        </Routes>
      </BrowserRouter>
      
    </div>
  );
}

export default App;
