import Layout from '../../components/general/layout'
import { Button, Container, Row, Col } from 'reactstrap';
import './style.scss'

const WithStaticProps = () => (
    <Layout title="Tu sitio favorito de ropa online - Mismoprec.io">
        <section className="mp-upper-body">
            <Container>
                <Row>
                    <Col xs="12" lg="7">
                        <h1>No es una tienda, <br />Es tu sitio de ropa preferido</h1>
                        <p>Podrás encontrar y comparar prendas de distintas tiendas en un mismo lugar y al mismo precio de tu bolsillo</p>
                        <Button color="primary">Ver catálogo</Button>
                    </Col>
                    <Col xs={{ size: 0}} md={{ size: 5 }} className="d-none d-lg-block">
                        <img src={require('./../../static/images/illustrations/cover-image.svg')} width="350" height="350" />
                    </Col>
                </Row>
            </Container>
        </section>
    </Layout>
)



export default WithStaticProps
