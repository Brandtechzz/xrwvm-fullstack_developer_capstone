import React, { useState } from "react";
import "./Register.css";
import user_icon from "../assets/person.png"
import email_icon from "../assets/email.png"
import password_icon from "../assets/password.png"
import close_icon from "../assets/close.png"

const Register = () => {

  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setlastName] = useState("");
  const [errorMessage, setErrorMessage] = useState(""); // State for error messages

  const gohome = ()=> {
    window.location.href = window.location.origin;
  }

  const register = async (e) => {
    e.preventDefault(); // Prevent default form submission
    // Ensure this URL points to your Django backend
    const register_url = `${window.location.origin}/djangoapp/register/`; 

    const res = await fetch(register_url, {
        method: "POST", // Make sure this is POST
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            userName,
            password,
            firstName,
            lastName,
            email,
        }),
    });

    const json = await res.json(); // Parse JSON response
    if (res.ok) {
        sessionStorage.setItem('username', json.userName); // Store username on success
        window.location.href = window.location.origin; // Redirect to home
    } else {
        alert(json.error || "Registration failed."); // Show error if it fails
    }
};

  return(
    <div className="register_container" style={{width: "50%"}}>
      <div className="header" style={{display: "flex",flexDirection: "row", justifyContent: "space-between"}}>
          <span className="text" style={{flexGrow:"1"}}>SignUp</span> 
          <div style={{display: "flex",flexDirection: "row", justifySelf: "end", alignSelf: "start" }}>
          <a href="/" onClick={()=>{gohome()}} style={{justifyContent: "space-between", alignItems:"flex-end"}}>
            <img style={{width:"1cm"}} src={close_icon} alt="X"/>
          </a>
          </div>
          <hr/>
        </div>

        <form onSubmit={register}>
        <div className="inputs">
          <div className="input">
            <img src={user_icon} className="img_icon" alt='Username'/>
            <input type="text"  name="username" placeholder="Username" className="input_field" onChange={(e) => setUserName(e.target.value)}/>
          </div>
          <div>
            <img src={user_icon} className="img_icon" alt='First Name'/>
            <input type="text"  name="first_name" placeholder="First Name" className="input_field" onChange={(e) => setFirstName(e.target.value)}/>
          </div>

          <div>
            <img src={user_icon} className="img_icon" alt='Last Name'/>
            <input type="text"  name="last_name" placeholder="Last Name" className="input_field" onChange={(e) => setlastName(e.target.value)}/>
          </div>

          <div>
            <img src={email_icon} className="img_icon" alt='Email'/>
            <input type="email"  name="email" placeholder="email" className="input_field" onChange={(e) => setEmail(e.target.value)}/>
          </div>

          <div className="input">
            <img src={password_icon} className="img_icon" alt='password'/>
            <input name="psw" type="password"  placeholder="Password" className="input_field" onChange={(e) => setPassword(e.target.value)}/>
          </div>

        </div>
        <div className="submit_panel">
          <input className="submit" type="submit" value="Register"/>
        </div>
      </form>
      </div>
  )
}

export default Register;
