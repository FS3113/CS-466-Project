import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import {Button} from "@material-ui/core";

function App() {
  const [seq1, setSeq1] = useState('');
  const [seq2, setSeq2] = useState('');
  const [match, setMatch] = useState('');
  const [mismatch, setMismatch] = useState('');
  const [gap, setGap] = useState('');

  async function submit() {
    console.log(seq1);
    console.log(seq2);

    await fetch('/get', {method:"POST", body:JSON.stringify({}), headers:{"content_type":"application/json"}})
    .then(res => res.json()).then( async data => {
      console.log(data);
    })
  }

  return (
    <div className="homeOuterContainer">
      <div className="homeInnerContainer"> 
      <h1 className="heading">Visulization of Hirschberg Algorithm</h1>
          <div>
              <input placeholder="Sequence 1" className="input" type="text" onChange={(event) => setSeq1(event.target.value)} /> 
              <input placeholder="Sequence 2" className="input mt-20" type="text" onChange={(event) => setSeq2(event.target.value)} />
              <input placeholder="Match" className="input mt-20" type="text" onChange={(event) => setMatch(event.target.value)} />
              <input placeholder="Misatch" className="input mt-20" type="text" onChange={(event) => setMismatch(event.target.value)} />
              <input placeholder="Gap" className="input mt-20" type="text" onChange={(event) => setGap(event.target.value)} />
          </div>
          <button className="button mt-20" type="submit" onClick={submit}>Submit</button>     
      </div>
      
    </div>
  );
}

export default App;
