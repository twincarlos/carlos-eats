import { useSelector } from "react-redux";
import LoggedIn from "./LoggedIn";
import NotLoggedIn from './NotLoggedIn';

function NavBar() {
    const user = useSelector(state => state.session.user);

    return user ? <LoggedIn user={user}/> : <NotLoggedIn />;
}

export default NavBar;
