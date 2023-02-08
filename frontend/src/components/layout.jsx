import { React } from 'react';
import { Outlet, Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import { observer } from 'mobx-react';

function Layout(props) {
    
    const Navigate = useNavigate();

    function searchUser(event) {
        let text = document.getElementById('search');
        if (text.value===""){
            return;
        }
        Navigate(`/search/${text.value}`);
        
    }

    return (
        <div className='main-div'>
            <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                <Link to='/' className="navbar-brand">ChatApp</Link>
                <ul className="navbar-nav mr-auto">
                    <li className="nav-item active"><Link className="nav-link" to='/'>Home</Link></li>
                    <li className='nav-item active'><a href="/accounts/logout" className='nav-link'>Logout</a></li>
                </ul>
                <legend>Logged in as {props.User.username}</legend>
                <input type="text" id='search' /><button onClick={searchUser}>Search</button>
            </nav>
            <Outlet />
        </div>
    )
}

export default observer(Layout);