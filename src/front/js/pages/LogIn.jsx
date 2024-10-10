import React, { useContext, useState } from "react";
import { Context } from "../store/appContext.js";
import { useNavigate } from "react-router-dom";

export const LogIn = () => {
    const { actions } = useContext(Context);
    const [credentials, setCredentials] = useState({
        email: '',
        password: ''
    });

    const [error, setError] = useState("");
    const navigate = useNavigate();

    const handleChange = (e) => {
        setCredentials({
            ...credentials,
            [e.target.name]: e.target.value
        });
    };

    const handleLogin = async (e) => {
        e.preventDefault();
        const result = await actions.login(credentials);
        if (result.token) {
            console.log("Inicio de sesión correcto");
            navigate("/");
        } else {
            console.log("Error al iniciar sesión");
            setError("Error al iniciar sesión. Por favor, verifica tus credenciales.");
        }
    };

    return (
        <div className="container mt-5 mx-auto">
            <div className="row">
                <div className="col-md-6">
                    <div className="card shadow">
                        <div className="card-body">
                            <form onSubmit={handleLogin}>
                                <div className="form-group mb-3">
                                    <label htmlFor="email" className="form-label">
                                        Correo electrónico
                                    </label>
                                    <input
                                        type="email"
                                        className="form-control"
                                        id="email"
                                        name="email"
                                        value={credentials.email}
                                        onChange={handleChange}
                                        placeholder="Ingresa tu correo electrónico"
                                        required
                                    />
                                </div>
                                <div className="form-group mb-3">
                                    <label htmlFor="password" className="form-label">
                                        Contraseña
                                    </label>
                                    <input
                                        type="password"
                                        className="form-control"
                                        id="password"
                                        name="password"
                                        value={credentials.password}
                                        onChange={handleChange}
                                        placeholder="Ingresa tu contraseña"
                                        required
                                    />
                                </div>
                                {error && <p className="text-danger text-center">{error}</p>}
                                <div className="d-grid">
                                    <button type="submit" className="btn btn-primary">
                                        Iniciar sesión 
                                    </button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};
