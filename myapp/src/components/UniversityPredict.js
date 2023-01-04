import React from 'react'

export default function UniversityPredict(props) {
  return (
    <div>

        <h5>University name : {props.uniname}</h5>
        <h5>Acceptance probability : {props.prediction}</h5>
        <br/>
    </div>
  )
}
