import { React, useState, useEffect } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { observer } from 'mobx-react';

import Home from './components/home';
import Layout from './components/layout';
import ChatPage from './components/chatPage';
import SearchPage from './components/searchPage';

function App(props) {
  useEffect(() => {
    fetch('http://localhost:8000/api/user-data')
          .then((response) => response.json())
          .then((data) => {
              props.User.setUsername(data.username);
    });
  }, [])
  //console.log(window.location.href);
  return (

    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Layout socket={props.socket} User={props.User} />}>
          <Route index element={<Home socket={props.socket} User={props.User} />} />
          <Route path='chat/:chattingUser' element={<ChatPage socket={props.socket} User={props.User} />} />
          <Route path='search/:queryText' element={<SearchPage socket={props.socket} User={props.User} />} />
        </Route>  
      </Routes> 
    </BrowserRouter>
  );
}

export default observer(App);
