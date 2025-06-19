import React, { useEffect, useState } from 'react';

function App() {
  const [message, setMessage] = useState('');
  const [echoResponse, setEchoResponse] = useState(null);

  useEffect(() => {
    fetch('http://localhost:5000/api/message')
      .then(res => res.json())
      .then(data => setMessage(data.message));
  }, []);

  const sendData = async () => {
    const res = await fetch('http://localhost:5000/api/echo', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: 'Hi Flask' })
    });
    const data = await res.json();
    setEchoResponse(data);
  };

  return (
    <div>
      <h1>{message}</h1>
      <button onClick={sendData}>Send POST</button>
      {echoResponse && <pre>{JSON.stringify(echoResponse, null, 2)}</pre>}
    </div>
  );
}

export default App;
