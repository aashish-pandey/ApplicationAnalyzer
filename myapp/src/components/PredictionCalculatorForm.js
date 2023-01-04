import React, { useState } from 'react'
import { Navigate, useNavigate } from 'react-router-dom';

export default function PredictionCalculatorForm() {

    const [user, setUser] = useState([]);
    const navigate = useNavigate();

    const fetchData = async (urlstr) => {
        return await fetch(urlstr)
            .then((response) => response.json())
            
    }

   

    async function handleFormSubmit(e){
        e.preventDefault();
        var cgpa = e.target[0].value;
        var quant = e.target[1].value;
        var verbal = e.target[2].value;
        var toefl = e.target[3].value;
        var paper = e.target[4].value;
        var work = e.target[5].value;

        var urlstr = 'http://127.0.0.1:8000/?cgpa=' + cgpa 
        + '&quant=' + quant +
                '&verbal=' + verbal + '&toefl='+toefl+'&paper='+paper+'&work='+work


        var ur = await fetchData(urlstr);

        // console.log(ur[0]['University_names'])
        
        navigate('/uniPredictions', {state :{ur: ur}})
        
    }
    

  return (
    <div>

        
        PredictionCalculatorForm

        <form onSubmit={handleFormSubmit} method="get">

        Enter CGPA:<br/>
        <input type="text" name="cgpa"/><br/>

        Enter Quant Score:<br/>
        <input type="text" name="quant"/><br/>

        Enter Verbal Score:<br/>
        <input type="text" name="verbal"/><br/>

        Enter TOEFL Score: <br/>
        <input type="text" name="toefl"/><br/>

        Enter Number of papers published: <br/>
        <input type="text" name="paper_pub"/><br/>

        Enter Work experience in months: <br/>
        <input type="text" name="work_ex"/><br/>

        <input type="submit" value="submit"/>

    </form>


    </div>
  )
}
