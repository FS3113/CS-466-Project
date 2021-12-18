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
          <div className="inputContainer">
              <label>Sequence 1</label> 
              <input placeholder="Sequence 1" className="textInput" type="text" onChange={(event) => setSeq1(event.target.value)} /> 
              <label>Sequence 2</label> 
              <input placeholder="Sequence 2" className="textInput mt-20" type="text" onChange={(event) => setSeq2(event.target.value)} />
              <label>Match</label> 
              <input placeholder="Match" className="numberInput mt-20" type="number" value="1" onChange={(event) => setMatch(event.target.value)} />
              <label>Misatch</label> 
              <input placeholder="Misatch" className="numberInput mt-20" type="number" value="-1" onChange={(event) => setMismatch(event.target.value)} />
              <label>Gap</label> 
              <input placeholder="Gap" className="numberInput mt-20" type="number" value="-1" onChange={(event) => setGap(event.target.value)} />
          </div>
          <button className="button mt-20" type="submit" onClick={submit}>Submit</button>     
      </div>
      
    </div>
  );
}

export default App;
