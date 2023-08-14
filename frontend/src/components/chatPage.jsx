import { React, useEffect, useRef } from 'react';
import { useParams } from 'react-router-dom';
import { observer } from 'mobx-react';


function ChatPage(props) {
    const messageDOM = document.getElementById('message')
    const scrollRef = useRef(messageDOM);
    const {chattingUser} = useParams();
    if (props.User.currentMessages[chattingUser] === undefined) {
        props.User.currentMessages[chattingUser] = [];
    }

    useEffect(() => {
        scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
        fetch(`http://localhost:8000/api/get-message?reciever=${chattingUser}`)
            .then((response) => response.json())
            .then((data) => {
                console.log('chattingUser is : ' + chattingUser);
                console.log(JSON.stringify(data));
                props.User.appendCurrentMessage(data);
        });
    }, []);

    function sendMessage() {
        let text = document.getElementById('chattext');
        
        props.socket.send(JSON.stringify({
            type: 'message',
            sender: props.User.username,
            reciever: chattingUser,
            content: text.value,
        }));
        props.User.appendCurrentMessage({sender: props.User.username, reciever: chattingUser, content: text.value, created_at: new Date().toISOString()});
        text.value = '';  
    }

    return (
        <div className='main-box'>
            <h1>Chat</h1>
            <div className='main-content' id='message'>
                {props.User.currentMessages[chattingUser].map((message, key) => {
                    return (
                        <div className='message-container' key={key}>
                            <h6>{message.sender}</h6>
                            <p>{message.content}</p>
                            <hr />
                        </div>
                    )
                })}
                
            </div>
            <div ref={scrollRef} className="footer">
                <textarea name="chattext" id="chattext" className='chat-textarea'></textarea>
                <button className='chat-btn' onClick={sendMessage}>Send</button>
            </div>
        </div>
    )
}

export default observer(ChatPage);