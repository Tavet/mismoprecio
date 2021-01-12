import Layout from '../../components/general/Layout'
import { Button, Container, Row, Col } from 'reactstrap';
import './style.scss'

const WithStaticProps = () => (
    <Layout title="Tu sitio favorito de ropa online - Mismoprec.io">
        <section className="upper-body">
            <Container>
                <Row>
                    <Col xs="6" md="7">
                        <h1>RAMA FEATURE-FRONTEND PAPA JIJI</h1>
                        <p>Podrás encontrar y comparar prendas de distintas tiendas en un mismo lugar y al mismo precio de tu bolsillo</p>
                        <Button color="primary">Ver catálogo</Button>
                    </Col>
                    <Col>
                        <img src={require('./../../static/images/illustrations/cover-image.svg')} width="350" height="350" />
                    </Col>
                </Row>
            </Container>
        </section>
    </Layout>
)



export default WithStaticProps
