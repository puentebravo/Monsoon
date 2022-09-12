import React from "react";
import "./header.css"


function Header() {
    return (
        <nav className="container mx-auto h-14 position: sticky top-0 drop-shadow-2xl border-b-4 border-black" id="header">
            <p className="ml-6 text-white text-2xl first-letter:text-yellow-400 py-3">Monsoon</p>
        </nav>
    )
}

export default Header;