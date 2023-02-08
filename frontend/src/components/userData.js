import { makeObservable, action, observable } from 'mobx';

class UserData {
    username = 'none'
    chatUsers = []
    messages = {}
    currentMessages = {}

    constructor(socket) {
        this.clientSocket = socket;
        makeObservable(this, {
            currentMessages: observable,
            addToMessages: action,
            username: observable,
            chatUsers: observable,
            messages: observable,
            addMessage: action,
            addUser: action,
            setUsername: action,
            appendCurrentMessage: action,

        });
        this.clientSocket.onmessage = this.addToMessages;
    }
    
    addToMessages = (message) => {
        console.log('before' + JSON.stringify(message));
        message = JSON.parse(message.data);
        if (this.currentMessages[message.sender] === undefined) {
            this.currentMessages[message.sender] = [];
        }
        console.log('the parsed data is: ' + JSON.stringify(message));
        this.currentMessages[message.sender].push(message);
        this.messages[message.sender] = message.content;
    }

    appendCurrentMessage(message) {
        if (Array.isArray(message)) {
            /*
            for (let i=0; i<message.length; i++) {
                this.currentMessages.push(message[i]);
            }*/
            if (message.length>0){
                if (message[0].sender === this.username){
                    this.currentMessages[message[0].reciever] = message;
                }else {
                    this.currentMessages[message[0].sender] = message;
                }
            }else {
            }
        }else {
            this.messages[message.reciever] = message.content;
            console.log(JSON.stringify(this.messages));
            this.currentMessages[message.reciever].push(message);
        }
    }

    setUsername(name) {
        this.username = name;
    }

    addMessage(message) {
        if (Array.isArray(message)){
            for (let i=0; i< message.length; i++) {
                this.messages[message[i].user] = message[i].content;
            }
        } else {
            this.messages[message.user] = message.content;
        }
    }

    addUser(user) {
        if (this.chatUsers.includes(user.username)) {
            return;
        }
        this.chatUsers.push(user.username);
    }
}



export default UserData;