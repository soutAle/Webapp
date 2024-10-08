import React, { useContext } from "react";
import { Link, useNavigate } from "react-router-dom";
import { Context } from "../store/appContext";

export const Navbar = () => {
	const { store, actions } = useContext(Context);
	const navigate = useNavigate();
	const handleLogOutRedirect = () => {
		actions.logOut()
		navigate("/")
	}

	return (
		<nav className="navbar navbar-dark bg-dark">
			<div className="container-fluid">
				<Link className="navbar-brand ms-3" to={"/"}>
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
					className="offcanvas offcanvas-end text-bg-dark"
					tabIndex="-1"
					id="offcanvasDarkNavbar"
					aria-labelledby="offcanvasDarkNavbarLabel"
				>
					<div className="offcanvas-header bg-dark">
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
					<div className="offcanvas-body bg-dark">
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
										<Link className="dropdown-item" to={"/"}>
											Action
										</Link>
									</li>
									<li>
										<Link className="dropdown-item" to={"/"}>
											Another action
										</Link>
									</li>
									<li>
										<hr className="dropdown-divider" />
									</li>
									<li>
										<Link className="dropdown-item" to={"/"}>
											Something else here
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

				<div className="d-none d-md-flex">
					<ul className="navbar-nav-text d-flex justify-content-end align-items-end flex-grow-1 pe-5">
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
									<Link className="dropdown-item" to={"/"}>
										Action
									</Link>
								</li>
								<li>
									<Link className="dropdown-item" to={"/"}>
										Another action
									</Link>
								</li>
								<li>
									<hr className="dropdown-divider" />
								</li>
								<li>
									<Link className="dropdown-item" to={"/"}>
										Something else here
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
