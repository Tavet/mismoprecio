import React from 'react'
import { Container, Row, Col } from 'reactstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faTwitterSquare, faInstagramSquare } from '@fortawesome/free-brands-svg-icons'
import { Timeline } from 'react-twitter-widgets'
import './style.scss';

const Footer = () => (
    <footer className="mp-footer">
        <section className="mp-footer-container">
            <Container>
                <Row>
                    <Col xs={{ size: 12, order: 3 }} md={{ size: 3, order: 1 }}className="text-left align-self-end">
                        <p><FontAwesomeIcon icon={faTwitterSquare} size="2x" /> <FontAwesomeIcon icon={faInstagramSquare} size="2x" /></p>
                        <p><img src={require('./../../../static/images/mismoprecio.svg')} alt="Logo" height="16" width="auto" className="logo" /> Mismo Precio &copy; 2021</p>
                    </Col>
                    <Col xs={{ size: 12, order: 2 }} md={{ size: 4, order: 2 }} className="text-left align-self-end">
                        <p>Mapa del sitio</p>
                    </Col>
                    <Col xs={{ size: 12, order: 1 }} md={{ size: 5, order: 3 }} className="align-self-end">
                        <Timeline
                            dataSource={{
                                sourceType: 'profile',
                                screenName: 'ElonMusk'
                            }}
                            options={{
                                height: '450',
                                theme: 'dark'
                            }}
                        />
                    </Col>
                </Row>
            </Container>
        </section>
    </footer>
)

export default Footer
