import React, { useState } from 'react'
import {
    Collapse,
    Navbar,
    NavbarToggler,
    NavbarBrand,
    Nav,
    NavItem,
    NavLink
} from 'reactstrap';
import './style.scss'

const Navigation = () => {
    const [isOpen, setIsOpen] = useState(false);
    const toggle = () => setIsOpen(!isOpen);
    return (
        <Navbar light expand="md">
            <NavbarBrand href="/"><img src={require('./../../../static/images/mismoprecio.svg')} alt="logo" width="16" height="16" /> Mismo <span>Precio</span></NavbarBrand>
            <NavbarToggler onClick={toggle} />
            <Collapse isOpen={isOpen} navbar>
                <Nav className="ml-auto" navbar>
                    <NavItem>
                        <NavLink href="/inicio">Inicio</NavLink>
                    </NavItem>
                    <NavItem>
                        <NavLink href="/catalogo">Catálogo</NavLink>
                    </NavItem>
                    <NavItem>
                        <NavLink href="#">Outfits <span className="soon">¡Muy pronto!</span></NavLink>
                    </NavItem>
                </Nav>
            </Collapse>
        </Navbar>
    )
}

export default Navigation
