import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import { w3cwebsocket as W3CWebSocket } from "websocket";
import 'bootstrap/dist/css/bootstrap.min.css';
import App from './App';
import UserData from './components/userData';

const clientSocket = new W3CWebSocket('ws://localhost:8000/ws/socket-server');

const User = new UserData(clientSocket);

clientSocket.onopen = () => {
  console.log("socket connected!");
}

clientSocket.onclose = () => {
  console.log('socket closed!');
}







const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App socket={clientSocket} User={User} />
  </React.StrictMode>
);
