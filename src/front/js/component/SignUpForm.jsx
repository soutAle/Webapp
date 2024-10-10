import React, { useState, useContext, useEffect } from "react";
import { Context } from "../store/appContext";
import { useNavigate } from "react-router-dom";

export const SignUpForm = () => {
    const { actions, store } = useContext(Context);
    const [formData, setFormData] = useState({
        name: "",
        last_name: "",
        email: "",
        password: "",
        telephone: "",
        country: "",
        photo: "",
    });
    const [error, setError] = useState(null);
    const [successMessage, setSuccessMessage] = useState(null); 
    const navigate = useNavigate();

    useEffect(() => {
        if (store.error) {
            setError(store.error);
        } else {
            setError(null);
        }
        return () => setError(null);
    }, [store.error]);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(null);

        const result = await actions.Signup(formData);

        if (result.success) {
            setSuccessMessage("Te has registrado correctamente");
            setTimeout(() => {
                navigate("/login");
            }, 1500);
        } else {
            setError(result.error);
        }
    };

    return (
        <div className="container mt-5">
            <div className="row justify-content-center">
                <div className="col-md-6">
                    <div className="card shadow">
                        <div className="card-body">
                            {successMessage && <p className="alert alert-success text-success text-center">{successMessage}</p>}
                            <form onSubmit={handleSubmit}>
                                <div className="form-group mb-3">
                                    <label htmlFor="name" className="form-label">
                                        Nombre
                                    </label>
                                    <input
                                        type="text"
                                        className="form-control"
                                        id="name"
                                        name="name"
                                        value={formData.name}
                                        onChange={handleChange}
                                        placeholder="Ingresa tu nombre"
                                        required
                                    />
                                </div>
                                <div className="form-group mb-3">
                                    <label htmlFor="last_name" className="form-label">
                                        Apellido
                                    </label>
                                    <input
                                        type="text"
                                        className="form-control"
                                        id="last_name"
                                        name="last_name"
                                        value={formData.last_name}
                                        onChange={handleChange}
                                        placeholder="Ingresa tu apellido"
                                        required
                                    />
                                </div>
                                <div className="form-group mb-3">
                                    <label htmlFor="email" className="form-label">
                                        Correo electrónico
                                    </label>
                                    <input
                                        type="email"
                                        className="form-control"
                                        id="email"
                                        name="email"
                                        value={formData.email}
                                        onChange={handleChange}
                                        placeholder="Ingresa tu correo electrónico"
                                        required
                                    />
                                </div>
                                <div className="form-group mb-3">
                                    <label htmlFor="telephone" className="form-label">
                                        Teléfono
                                    </label>
                                    <input
                                        type="tel"
                                        className="form-control"
                                        id="telephone"
                                        name="telephone"
                                        value={formData.telephone}
                                        onChange={handleChange}
                                        placeholder="Ingresa tu teléfono"
                                        required
                                    />
                                </div>
                                <div className="form-group mb-3">
                                    <label htmlFor="country" className="form-label">
                                        País
                                    </label>
                                    <input
                                        type="text"
                                        className="form-control"
                                        id="country"
                                        name="country"
                                        value={formData.country}
                                        onChange={handleChange}
                                        placeholder="Ingresa tu país"
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
                                        value={formData.password}
                                        onChange={handleChange}
                                        placeholder="Ingresa tu contraseña"
                                        required
                                    />
                                </div>
                                <div className="form-group mb-3">
                                    <label htmlFor="photo" className="form-label">
                                        Foto (URL)
                                    </label>
                                    <input
                                        type="text"
                                        className="form-control"
                                        id="photo"
                                        name="photo"
                                        value={formData.photo}
                                        onChange={handleChange}
                                        placeholder="Ingresa la URL de tu foto"
                                    />
                                </div>
                                {error && <p className="text-danger text-center">{error}</p>}
                                <div className="d-grid">
                                    <button type="submit" className="btn btn-primary">
                                        Registrarse
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
