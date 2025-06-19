import React, { useEffect, useState } from 'react';

function App() {
  const [message, setMessage] = useState('');
  const [echoResponse, setEchoResponse] = useState(null);
  const [inputText, setInputText] = useState('Hi Flask');

  useEffect(() => {
    fetch('http://localhost:5000/api/message')
      .then(res => res.json())
      .then(data => setMessage(data.message));
  }, []);

  const sendData = async () => {
    const res = await fetch('http://localhost:5000/api/echo', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: inputText })
    });
    const data = await res.json();
    setEchoResponse(data);
  };

  return (
    <div>
      <h1>{message}</h1>
      <div>
        <input 
          type="text" 
          value={inputText} 
          onChange={(e) => setInputText(e.target.value)} 
        />
        <button onClick={sendData}>Send POST</button>
      </div>
      {echoResponse && <pre>{JSON.stringify(echoResponse, null, 2)}</pre>}
    </div>
  );
}

export default App;