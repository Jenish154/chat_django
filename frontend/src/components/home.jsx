import { React, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { observer } from 'mobx-react';

function Home(props) {

    useEffect(() => {
        fetch('http://localhost:8000/api/get-chats')
            .then((response) => response.json())
            .then((data) =>{
                props.User.addMessage(data);
                
            })
    }, [props.User.messages])

    const Navigate = useNavigate();
    function redirect(username) {
        
        Navigate(`/chat/${username}`);
    }
    return (
        <div className='main-content'>
            <h1>Your Chats</h1>
            <hr />
            {Object.entries(props.User.messages).map(([key, value]) => {
                return (
                    <div key={key}>
                        <button className="home-user-button" onClick={() => redirect(key)}><h4>{key}</h4></button>
                        <p>{value}</p>
                        <hr />
                    </div>
                );
            })}
        </div>
    )
}

export default observer(Home);