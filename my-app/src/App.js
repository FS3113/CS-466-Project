import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import {Button} from "@material-ui/core";

function App() {
  const [tmp, setTmp] = useState('3113');
  function handleChange(event){ setTmp(event.target.value); console.log(tmp)}

  async function submit() {
    await fetch('/get', {method:"POST", body:JSON.stringify({}), headers:{"content_type":"application/json"}})
    .then(res => res.json()).then( async data => {
      console.log(data);
    })
  }

  return (
    <div className="App">
      <form>
        <label>
          Name:
          <input type="text" value={tmp} onChange={handleChange}/>
        </label>
      </form>
      <div>
        <Button color="secondary" onClick={submit}>
            Submit
        </Button>
      </div>
    </div>
  );
}

export default App;
