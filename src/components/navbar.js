import React from "react";
import './navbar.styles.scss';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUser } from '@fortawesome/free-solid-svg-icons';
import { Link } from "react-router-dom";

class Navbar extends React.Component {

    componentDidMount() {
        window.addEventListener("scroll", this.handleScrollTop);
    }

    componentWillUnmount() {
        window.removeEventListener("scroll", this.handleScrollTop);
    }

    handleScrollTop = () => {
        if (window.scrollY > 20) {
            document.querySelector(".navbar-container").className = "navbar-container scroll";
        }
        else {
            document.querySelector(".navbar-container").className = "navbar-container";
        }
    };

    render() {
        return (
            <div className="navbar-container">
                <div className="navbar-container-md">
                    <Link className="navbar-text" to='/'><h3 className="navbar-text navbar-title">REAML</h3></Link>
                </div>
            </div>
        )
    }
}

export default Navbar;