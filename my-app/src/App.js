import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [seq1, setSeq1] = useState('');
  const [seq2, setSeq2] = useState('');
  const [match, setMatch] = useState('');
  const [mismatch, setMismatch] = useState('');
  const [gap, setGap] = useState('');
  const [images, setImages] = useState({});
  const [tick, setTick] = useState(1);

  function importAll(dir) {
    let imgs = {};
    dir.keys().map((item, index) => { imgs[item.replace('./', '')] = dir(item); });
    return imgs;
  }

  useEffect(() => {
    const retImages = importAll(require.context('./assets', false, /\.(png|jpe?g|svg)$/));
    setImages(retImages)
  }, [tick])

  async function submit(event) {
    const content = {'seq1': seq1, 'seq2': seq2, 'match': match, 'mismatch': mismatch, 'gap': gap}
    await fetch('/get', {method:"POST", body:JSON.stringify(content), headers:{"content_type":"application/json"}})
    .then(res => res.json()).then( async data => {
      console.log(data)
      setTick(tick * -1)
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
              <input placeholder="Match" className="numberInput mt-20" type="number" onChange={(event) => setMatch(event.target.value)} />
              <label>Misatch</label> 
              <input placeholder="Misatch" className="numberInput mt-20" type="number" onChange={(event) => setMismatch(event.target.value)} />
              <label>Gap</label> 
              <input placeholder="Gap" className="numberInput mt-20" type="number" onChange={(event) => setGap(event.target.value)} />
          </div>
          <button className="button mt-20" type="submit" onClick={submit}>Submit</button>
          {
            Object.keys(images).map(function(keyName, keyIndex) {
              return (
                <img key={keyName} src={images[keyName]} />
              )
          })}
      </div>
    </div>
  );
}

export default App;
