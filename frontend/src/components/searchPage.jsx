import { React, useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { observer } from 'mobx-react';

function SearchPage(props) {
    let data;
    const Navigate = useNavigate();
    const [users, setUsers] = useState([]);

    const {queryText} = useParams();

    function redirect(username) {
        Navigate(`/chat/${username}`);
    }

    useEffect(() => {
        fetch(`http://localhost:8000/api/search-users?search_text=${queryText}`)
            .then((response) => response.json())
            .then((data) => {
                setUsers(data);
        });
    }, [queryText])


    if (users.length===0) {
        data = 'No such user found';
    } else {
        data = users.map((user, key) => {
            return (
                <div key={key}>
                    <button className='home-user-button' onClick={() => redirect(user.username)}><h4>{user.username}</h4></button>
                </div>
            )
        })
    }
    return (
        <div className='main-content'>
            {data}
        </div>
    )
}

export default observer(SearchPage);