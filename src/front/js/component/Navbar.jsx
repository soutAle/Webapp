import React, { useContext } from "react";
import { Link, useNavigate } from "react-router-dom";
import { Context } from "../store/appContext";
import "../../styles/navbar.css"; 
import { IoPersonCircleOutline, IoLogOutOutline } from "react-icons/io5";

export const Navbar = () => {
	const { store, actions } = useContext(Context);
	const navigate = useNavigate();
	const handleLogOutRedirect = () => {
		actions.logOut();
		navigate("/");
	};

	return (
		<nav className="navbar custom-navbar">
			<div className="container-fluid">
				<Link className="navbar-brand ms-3 text-white" to={"/"}>
					Finder
				</Link>
				<button
					className="navbar-toggler d-md-none"
					type="button"
					data-bs-toggle="offcanvas"
					data-bs-target="#offcanvasDarkNavbar"
					aria-controls="offcanvasDarkNavbar"
					aria-label="Toggle navigation"
				>
					<span className="navbar-toggler-icon"></span>
				</button>
				<div
					className="offcanvas offcanvas-end"
					tabIndex="-1"
					id="offcanvasDarkNavbar"
					aria-labelledby="offcanvasDarkNavbarLabel"
				>
					<div className="offcanvas-header">
						<h5 className="offcanvas-title text-white" id="offcanvasDarkNavbarLabel">
							Finder
						</h5>
						<button
							type="button"
							className="btn-close btn-close-white"
							data-bs-dismiss="offcanvas"
							aria-label="Close"
						></button>
					</div>
					<div className="offcanvas-body">
						<ul className="navbar-nav justify-content-end flex-grow-1 pe-3 mt-3">
							<li className="nav-item">
								<Link className="nav-link active" aria-current="page" to={"/"}>
									Home
								</Link>
							</li>
							<li className="nav-item">
								<Link className="nav-link" to={"/"}>
									Link
								</Link>
							</li>
							<li className="nav-item dropdown">
								<Link
									className="nav-link dropdown-toggle"
									to={"/"}
									role="button"
									data-bs-toggle="dropdown"
									aria-expanded={false}
								>
									Dropdown
								</Link>
								<ul className="dropdown-menu dropdown-menu-dark">
									<li>
										<Link className="dropdown-item" to={"/profiledeveloper"}>
											Perfil
										</Link>
									</li>
									<li>
										<Link className="dropdown-item" to={"/myoffers"}>
											Mis Ofertas
										</Link>
									</li>
									<li>
										<hr className="dropdown-divider" />
									</li>
									<li>
										<Link className="dropdown-item" to={"/"} onClick={handleLogOutRedirect}>
											Cerrar Sesión
										</Link>
									</li>
								</ul>
							</li>
						</ul>
						<form className="d-flex mt-3" role="search">
							<input
								className="form-control me-2"
								type="search"
								placeholder="Search"
								aria-label="Search"
							/>
							<button className="btn btn-success" type="submit">
								Search
							</button>
						</form>
					</div>
				</div>

				<div className="d-none d-md-flex pe-5">
					<ul className="navbar-nav-text d-flex justify-content-end align-items-end flex-grow-1 pe-5 list-unstyled mb-0">
						<li className="nav-item">
							<Link className="nav-link active" aria-current="page" to={"/"}>
								Inicio
							</Link>
						</li>
						<li className="nav-item">
							<Link className="nav-link" to={"/"}>
								Ofertas
							</Link>
						</li>
						<li className="nav-item">
							<Link className="nav-link active" aria-current="page" to={"/"}>
								Inicio
							</Link>
						</li>
						<li className="nav-item">
							<Link className="nav-link" to={"/"}>
								Link
							</Link>
						</li>
						<li className="nav-item dropdown">
							
							<Link
								className="nav-link mt-2"
								to={"/"}
								role="button"
								data-bs-toggle="dropdown"
								aria-expanded={false}
							>
								<IoPersonCircleOutline />
							</Link>
							<ul className="dropdown-menu">
								<li>
									<Link className="dropdown-item" to={"/"}>
										Perfil
									</Link>
								</li>
								<li>
									<Link className="dropdown-item" to={"/"}>
										Mis Ofertas
									</Link>
								</li>
								<li>
									<hr className="dropdown-divider" />
								</li>
								<li>
									<Link className="dropdown-item" to={"/"} onClick={handleLogOutRedirect}>
										<IoLogOutOutline />
										Cerrar Sesión
									</Link>
								</li>
							</ul>
						</li>
					</ul>
				</div>
			</div>
		</nav>
	);
};
