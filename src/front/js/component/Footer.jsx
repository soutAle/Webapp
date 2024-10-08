import React from "react";
import "../../styles/footer.css";
import { FaFacebook, FaInstagram, FaTwitter } from "react-icons/fa";
import { Link } from "react-router-dom";

export const Footer = () => (
	<footer className="footer py-2 mt-5">
		<div className="container-fluid">
			<div className="row text-center text-md-start">
				<div className="col-md-6 mb-3 mb-md-0">
					<div className="text-footer d-flex flex-column flex-md-row justify-content-center justify-content-md-start align-items-center align-items-md-start">
						<ul className="list-unstyled d-flex flex-column text-center flex-md-row mt-3">
							<li>
								<Link className="me-3 mb-2 mb-md-0 footer-link" to="/about">
									Sobre nosotros
								</Link>
							</li>
							<li>
								<Link className="me-3 mb-2 mb-md-0 footer-link" to="/contact">
									Contáctanos
								</Link>
							</li>
							<li>
								<Link className="me-3 mb-2 mb-md-0 footer-link" to="/privacy-policy">
									Política de privacidad
								</Link>
							</li>
							<li>
								<Link className="me-3 mb-2 mb-md-0 footer-link" to="/cookie-policy">
									Política de cookies
								</Link>
							</li>
							<li>
								<Link className="me-3 mb-2 mb-md-0 footer-link" to="/copyright-policy">
									Política de Copyright
								</Link>
							</li>
							<li>
								<Link className="footer-link" to="/legal-terms">
									Condiciones legales
								</Link>
							</li>
						</ul>
					</div>

				</div>

				<div className="col-md-6 d-flex justify-content-center justify-content-md-end align-items-center">
					<span className="me-3 mb-3 fs-4">¡Síguenos!</span>
					<ul className="footer-icons list-unstyled d-flex">
						<li className="me-3">
							<a
								className="rrss-icons"
								href="https://www.facebook.com/groups/fitiniespana/?locale=es_LA"
								target="_blank"
								rel="noopener noreferrer"
							>
								<FaFacebook />
							</a>
						</li>
						<li className="me-3">
							<a
								className="rrss-icons"
								href="https://www.instagram.com/empleos_espana.es"
								target="_blank"
								rel="noopener noreferrer"
							>
								<FaInstagram />
							</a>
						</li>
						<li className="me-3">
							<a
								className="rrss-icons"
								href="https://x.com/empleocero"
								target="_blank"
								rel="noopener noreferrer"
							>
								<FaTwitter />
							</a>
						</li>
					</ul>
				</div>
			</div>
		</div>
	</footer>
);
