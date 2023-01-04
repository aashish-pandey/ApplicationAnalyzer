import React from 'react'
import { useLocation, useNavigate, useNavigation, Link } from 'react-router-dom'
import UniversityPredict from './UniversityPredict'

export default function UniversityPredictions(props) {
    const navigate = useNavigate();
    const location = useLocation()
    const state = location.state
    const uls = state.ur

    // console.log(props.location)
    const handleBackToCalculator = ()=>{
        // navigate('http://localhost:3000/')
        
        
    }
  return (
    <div>
        <div>
            <button><Link to="/">Back To My Calculator</Link></button>
        </div>
        <h1>Your curated List of universities is:</h1>
        {uls.map(ul=>(
            <UniversityPredict uniname = {ul['University_names']} prediction={ul['Probabilty_of_acceptance']}/>
        ))}


    </div>
  )
}
